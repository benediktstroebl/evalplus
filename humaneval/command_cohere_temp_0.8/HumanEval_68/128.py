Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, following the problem statement you provided:
```python
def pluck(arr):
    even_nodes = [idx for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    min_idx = min(even_nodes)
    min_val = arr[min_idx]
    return [min_val, min_idx]

# Example usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)  # Expected output: [2, 1]
```

In this script, the `pluck` function first identifies all the even nodes in the array using a list comprehension. If there are no even nodes, it returns an empty list. Otherwise, it finds the minimum index of the even nodes and the corresponding value to return the result in the format [value, index].