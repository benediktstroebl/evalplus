Here's a Python script that solves the given problem with an efficient approach using generators, without the need for lists, and with a small memory footprint:
```python
def pluck(arr):
    even_nodes = (x for x in arr if x % 2 == 0)
    return ([x, idx] for (idx, x) in enumerate(min(even_nodes, key=lambda x: x)), None)
```

The script uses Python's generator expression and method shorthand, `enumerate`, for efficient iteration and finding the smallest even node. The generators do not build up memory-intensive intermediate lists, passing the smallest even node and its index to the final `[x, idx]` generator, which creates the desired output list. The `key=lambda x: x` argument to `min` ensures the node is sorted by value, not index.

This approach significantly reduces memory usage when dealing with large arrays, as it only generates the necessary results on-the-fly without storing everything in memory at once.