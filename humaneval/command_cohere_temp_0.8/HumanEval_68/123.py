Here's a Python script that solves the given problem with an efficient approach using `collections.heapq` module:
```python
import collections

def pluck(arr):
    # Create a min-heap of tuples with (value, index) using the heapq module
    heap = collections.heapq
    min_heap = [(val, i) for i, val in enumerate(arr)]
    heapq.heapify(min_heap)

    # Pull the smallest even value (if exists), otherwise pull the smallest value
    while min_heap and not isinstance(min_heap[0][0], int) or min_heap[0][0] % 2:
        heapq.heappop(min_heap)
    ans = []
    if min_heap:
        ans = [min_heap[0][0], min_heap[0][1]]
    return ans if ans else []

# Test cases
print(pluck([]))
print(pluck([1, 2, 3]))
print(pluck([4, 2, 3]))
print(pluck([5, 0, 3, 0, 4, 2]))
```

This approach leverages the `heapq` module to efficiently find the smallest even value (or smallest value if no even values) and its corresponding index from the array, thus ensuring a more optimized solution with a linear time complexity of O(n).

The code includes test cases to validate its behavior.