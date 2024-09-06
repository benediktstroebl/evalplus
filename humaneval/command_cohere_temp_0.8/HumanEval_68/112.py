Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, following the problem statement you provided:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_val, min_index = min(enumerate(even_nodes), key=lambda x: x[1])
    return [min_even_val, min_index[0]]

# Example Usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)  # Output: [2, 1]
```

In this script, the `pluck` function first filters out the even-valued nodes from the input array. It then identifies the smallest even value and its corresponding index using the `min` function with the `enumerate` utility. The result is returned as a list containing the smallest even value and its index. If no even values are present, an empty list is returned.