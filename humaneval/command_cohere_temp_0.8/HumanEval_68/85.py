Here's a Python script that solves the given problem with an efficient approach using `collections.heapq` module:
```python
import heapq

def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes:
        # Use heapq to find the smallest even node and its index
        heap = [(n, i) for i, n in enumerate(even_nodes)]
        heapq.heapify(heap)
        smallest_node, smallest_index = heapq.heappop(heap)
        
        return [smallest_node, smallest_index]
    else:
        return []
```

The approach utilizes Python's `heapq` module to efficiently find the smallest even node and its index from the array. It first constructs a list of even nodes from the input array and then uses a min-heap to find the smallest even node along with its index. The `heappop` function retrieves the smallest element from the heap along with its index, providing the desired result.

The code is structured such that it can be readily executed and evaluated against the test cases provided in the prompt to ensure its correctness. You can copy and paste this code into a Python environment or IDE of your choice to test and validate its behavior against the example inputs.  If you'd like to delve deeper or explore more efficient approaches, let me know!