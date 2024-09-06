Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, in accordance with the problem statement:
```python
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if not even_nodes:
        return []
    min_value = min(even_nodes)
    min_index = even_nodes.index(min_value)
    return [min_value, min_index]
```

This function identifies even nodes using a list comprehension and calculates the minimum value from these even nodes. It then locates the index of the minimum value using the `index` method. The result is a list containing the minimum even value and its corresponding index.

The `if not even_nodes:` block ensures that if there are no even nodes in the array, an empty list is returned, adhering to the problem's requirement. 

This approach provides an efficient solution, with a time complexity of O(n) where n is the length of the input array.