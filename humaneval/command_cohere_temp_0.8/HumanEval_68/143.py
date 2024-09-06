Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch, adhering to the problem statement:
```python
def pluck(arr):
    even_nodes = [x for x in arr if x % 2 == 0]
    if not even_nodes:
        return []
    min_value = min(even_nodes)
    min_index = even_nodes.index(min_value)
    return [min_value, min_index]
```

This function identifies even nodes using a list comprehension and finds the minimum value using the `min` function. It then locates the index of the minimum value via the `index` method. The result is a list containing the minimum even value and its corresponding index.

Here's an example of how you can use the `pluck` function with a sample input:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)
```

For the input array `[4, 2, 3]`, the expected output is `[2, 1]`, indicating that node 2 with a value of 2 is plucked, and it occupies the first position in the array, at index 1.