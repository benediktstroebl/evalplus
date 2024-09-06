Here's a Python script that includes a function `pluck` which follows the logic of the problem:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]
```

This script includes a function `pluck` that takes an array as a parameter and follows these steps:
1. It collects all even numbers within the array.
2. If the list of even numbers is empty, the function returns an empty list too.
3. Otherwise, it finds the minimum even number and its index in the array.
4. Finally, it returns a list containing the minimum even number and its index. 

This solution follows the mandate that multiple nodes with the same smallest even value select the one with the smallest index.

The code is self-contained as it does not import any additional modules and can be run independently. You can test this code by calling the `pluck` function with different arrays and verifying that it produces the expected results.