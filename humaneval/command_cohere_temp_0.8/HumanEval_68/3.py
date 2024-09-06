Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch, adhering to the problem statement:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]
```

This script includes a standalone `pluck` function that accepts an array (`arr`) as input. It filters the array to isolate even nodes, then identifies the smallest even node, ultimately returning it along with its index in a list.

The code has been structured to be concise and readily interpretable, adhering to the problem statement and prevailing testing scenarios. Feel free to adopt it in your project or further customize it as required.  Should you want to delve deeper or explore additional scenarios, the provided base can serve as a robust foundation.