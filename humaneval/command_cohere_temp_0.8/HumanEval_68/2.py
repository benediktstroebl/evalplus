Here's a Python script that includes a function `pluck` that solves the problem:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if even_nodes:
        min_val = min(even_nodes)
        min_index = even_nodes.index(min_val)
        return [min_val, min_index]
    else:
        return []
```

This script defines a function `pluck()` that takes an array (`arr`) as input and returns a list containing the smallest even value in the array and its index in the array, or an empty list if no even values are found. The function first filters out the even numbers from the input array, then finds the minimum even number using the `min` function and its index using the `index` method. 

You can test this function using the examples provided in the problem statement to ensure it behaves as expected.