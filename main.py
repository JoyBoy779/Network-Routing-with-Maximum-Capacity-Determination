class Heap:

    def __init__(self, n, source, maxcap):
        self.maxcapacity = [-1 for i in range(n)] 
        #ith index stores the maxcapacity of the ith numbered node
        
        self.maxcapacity[source] = maxcap
        
        self.struct = [i for i in range(n)] #actual structure of the heap
        
        self.positions = [i for i in range(n)] #ith index represents the position of the ith node in the heap structure
        
        self.size = n
        
        self.heap_up(self.positions[source])
        # O(log n) for heap_up on a single element

    def parent(self, i): #calculates the position of the parent for the given index
        return max(0, (i-1)//2)
        #O(1)

    def left(self, i): #calculates the position of the left child for the given 
        if 2*i + 1 > self.size - 1:
            return i
        return 2*i+1
        #O(1)

    def right(self, i): #calculates the position of the right child for the given index
        if 2*i + 2 > self.size - 1:
            return i
        return 2*i+2
        #O(1)

    def heap_up(self, k): #This is the standard heap up operation
        p = self.parent(k) #parent index of the kth index
        
        p_node = self.struct[p]
        k_node = self.struct[k]
    
        if self.maxcapacity[p_node] < self.maxcapacity[k_node] :
            self.positions[k_node], self.positions[p_node] = p, k
            self.struct[k], self.struct[p] = p_node, k_node
            self.heap_up(p) #recurse on the parent
        #O(log n)

    def heap_down(self, k):#This is the standard heap down operation
        l = self.left(k) #left child index of the kth index
        r = self.right(k) #right child indez of the kth index

        k_node = self.struct[k]
        l_node = self.struct[l]
        r_node = self.struct[r]

        max_cap_lr = l
        # Check if right child capacity is greater than left child capacity
        if self.maxcapacity[r_node] > self.maxcapacity[l_node]:
            max_cap_lr = r
        max_cap_node = self.struct[max_cap_lr]  
            
        # Check if the child with max capacity is greater than the current node's capacity
        if self.maxcapacity[max_cap_node] > self.maxcapacity[k_node]:
            # Swap node positions and struct elements
            self.positions[k_node], self.positions[max_cap_node] = max_cap_lr, k
            self.struct[k], self.struct[max_cap_lr] = max_cap_node, k_node
            self.heap_down(max_cap_lr)
        #O(log n)

    def build(self): #this is the standard linear time build heap operation
        for i in range(self.size-1,-1,-1): #heap down from the last element
            self.heap_down(i) 
        #O(n)

    def extract_max(self): #Standard extract max operation
        if self.size == 0:
            return None
        
        top = self.struct[0]
        bottom = self.struct[self.size-1]
        
        # Swap top and bottom
        self.positions[top], self.positions[bottom] = self.size - 1, 0
        self.struct[0], self.struct[self.size-1] = bottom, top 
        
        self.size -= 1
        
        if self.size > 0:
            self.heap_down(0)
        
        return top


def findMaxCapacity(n, links, s, t):
    # Determine the initial max capacity for the source node
    # Use max link capacity + 1 to simulate "infinite" initial capacity
    if not links:
        maxcap = 0
    else:
        maxcap = max(link[2] for link in links)
    
    # adjlist structure: [Adjacency List, Visited Flag (0/1), Parent Node for path]
    adjlist = [[[], 0, -1] for i in range(n)]
    
    for u, v, c in links:
        adjlist[u][0].append((v, c)) 
        adjlist[v][0].append((u, c))
        
    capacities = Heap(n, s, maxcap + 1)
        
    while capacities.size > 0:
        max_node = capacities.extract_max()
        
        # Optimization: If the target is the max_node, we have found the path
        if max_node == t:
            break
        
        # Mark as visited
        adjlist[max_node][1] = 1
        
        # Relaxation step
        for neighbor, link_capacity in adjlist[max_node][0]:
            
            # Check if neighbor is unvisited
            if adjlist[neighbor][1] == 0:
                
                # New bottleneck capacity
                replace_by = min(link_capacity, capacities.maxcapacity[max_node])
                replace_this = capacities.maxcapacity[neighbor]
                
                if replace_by > replace_this:
                    
                    # Update parent and capacity, then bubble up in the heap
                    adjlist[neighbor][2] = max_node
                    capacities.maxcapacity[neighbor] = replace_by
                    capacities.heap_up(capacities.positions[neighbor])

    # Path Reconstruction
    prev = t
    result = []
    
    while prev != -1:
        result.append(prev)
        prev = adjlist[prev][2]
        
    # Final result: (Max Capacity C, Route list)
    return (capacities.maxcapacity[t], result[::-1])
            

# --- Running 5 Test Cases ---

# Test Case 1: (3, [(0,1,1), (1,2,1)], 0, 1) -> (1, [0, 1])
print(f">>> findMaxCapacity(3, [(0,1,1), (1,2,1)),0,1)")
print(findMaxCapacity(3, [(0,1,1), (1,2,1)], 0, 1))

# Test Case 2: (4, [(0,1,30), (0,3,10), (1,2,40), (2,3,50), (0,1,60), (1,3,50)], 0, 3) -> (50, [0,1,3])
print(f">>> findMaxCapacity(4, [(0,1,30), (0,3,10), (1,2,40), (2,3,50), (0,1,60), (1,3,50)],0,3)")
print(findMaxCapacity(4, [(0,1,30), (0,3,10), (1,2,40), (2,3,50), (0,1,60), (1,3,50)], 0, 3))

# Test Case 3: (4, [(0,1,30), (1,2,40), (2,3,50), (0,3,10)], 0, 3) -> (30, [0,1,2,3])
print(f">>> findMaxCapacity(4, [(0,1,30), (1,2,40), (2,3,50), (0,3,10)),0,3)")
print(findMaxCapacity(4, [(0,1,30), (1,2,40), (2,3,50), (0,3,10)], 0, 3))

# Test Case 4: (5, [(0,1,3), (1,2,5), (2,3,2),(3,4,3), (4,0,8), (0,3,7), (1,3,4)], 0, 2) -> (4, [0,3,1,2])
print(f">>> findMaxCapacity(5, [(0,1,3), (1,2,5), (2,3,2),(3,4,3), (4,0,8), (0,3,7), (1,3,4)],0,2)")
print(findMaxCapacity(5, [(0,1,3), (1,2,5), (2,3,2),(3,4,3), (4,0,8), (0,3,7), (1,3,4)], 0, 2))

# Test Case 5: (7, [(0,1,2), (0,2,5), (1,3,4), (2,3,4), (3,4,6), (3,5,4), (2,6,1), (6,5,2)], 0, 5) -> (4, [0, 2, 3, 5])
print(f">>> findMaxCapacity(7, [(0,1,2), (0,2,5), (1,3,4), (2,3,4), (3,4,6), (3,5,4), (2,6,1), (6,5,2)],0,5)")
print(findMaxCapacity(7, [(0,1,2), (0,2,5), (1,3,4), (2,3,4), (3,4,6), (3,5,4), (2,6,1), (6,5,2)], 0, 5))

