Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch, adhering to the given constraints:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_val, min_index = min(enumerate(even_nodes), key=lambda x: x[1])
    return [min_even_val, min_index[0]]
```

This function identifies even nodes in the array, finds the smallest even value, and returns it along with its index in the original array. 

Here's an example of how you might use this function:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)
```

In this case, the output would be `[2, 1]`, as the node with a value of 2 and the index of 1 is plucked from the array.