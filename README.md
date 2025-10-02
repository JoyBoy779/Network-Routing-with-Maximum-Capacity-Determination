# Network Routing with Maximum Capacity Determination

## 🚀 Project Overview

This project implements an efficient solution for the **Maximum Capacity Path** problem in a computer network. The goal is to determine the **largest possible packet size** (capacity $C$) that can be successfully transferred from a designated source router ($s$) to a target router ($t$), and to find the specific route that achieves this bottleneck capacity.

## 🎯 Problem Definition

Given a network of $N$ routers and $M$ bidirectional links, each with a specific capacity, we aim to find a path from a source router $s$ to a target router $t$. The capacity of any path is limited by the **minimum capacity link** along that path (the bottleneck).

The core task is to **maximize this bottleneck capacity** across all possible paths from $s$ to $t$.

## 💡 Algorithm and Implementation

The solution is built upon a fundamental graph algorithm adapted for this specific requirement:

1.  **Modified Dijkstra's Algorithm:** The core logic utilizes a modified version of **Dijkstra's algorithm**. Unlike standard Dijkstra's, which minimizes the cumulative path weight (distance), this adaptation **maximizes the minimum capacity** encountered on the path.
2.  **Max-Heap Priority Queue:** To achieve an efficient time complexity, a **Max-Heap** data structure is implemented and used as a priority queue. This heap prioritizes routers based on the **largest bottleneck capacity** found so far from the source.
3.  **Efficiency:** The implementation ensures the program runs efficiently, achieving a time complexity of $O(M \log N)$, where $M$ is the number of links (edges) and $N$ is the number of routers (nodes).

## 📁 Repository Contents

* `main.py`: Contains the main Python implementation, including the `Heap` class for the priority queue and the `findMaxCapacity` function.
* `README.md`: This file.

## 🛠️ Usage and Functionality

The main logic resides within the `findMaxCapacity` function.

### `findMaxCapacity(n, links, s, t)`

| Parameter | Description |
| :--- | :--- |
| `n` | The total number of routers in the network ($0$ to $n-1$). |
| `links` | A list of 3-tuples `(u, v, c)` representing a bidirectional link between router `u` and `v` with capacity `c`. |
| `s` | The source router identity. |
| `t` | The target router identity. |

### Return Value

The function returns a pair: `(C, route)`
* `C`: The largest capacity such that a packet of size $C$ can be transferred from $s$ to $t$.
* `route`: A list of router indices representing the path that achieves the capacity $C$.

---
## Examples Test Cases

The following test cases are taken directly from the assignment specification and demonstrate the required output format:

**Test Case 1**
```python
>>> findMaxCapacity(3, [(0,1,1), (1,2,1)), 0, 1)
(1, [0, 1])
```
**Test Case 2**
```python
>>> findMaxCapacity(4, [(0,1,30), (0,3,10), (1,2,40), (2,3,50), (0,1,60), (1,3,50)], 0, 3)
(50, [0, 1, 3])
```
**Test Case 3**
```python
>>> findMaxCapacity(4, [(0,1,30), (1,2,40), (2,3,50), (0,3,10)), 0, 3)
(30, [0, 1, 2, 3])
```
**Test Case 4**
```python
>>> findMaxCapacity(5, [(0,1,3), (1,2,5), (2,3,2),(3,4,3), (4,0,8), (0,3,7), (1,3,4)], 0, 2)
(4, [0, 3, 1, 2])
```
**Test Case 5**
```python
>>> findMaxCapacity(7, [(0,1,2), (0,2,5), (1,3,4), (2,3,4), (3,4,6), (3,5,4), (2,6,1), (6,5,2)], 0, 5)
(4, [0, 2, 3, 5])
```
