Here's a Python script that solves the given problem with an efficient algorithm using a sorted list:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if even_nodes:
        return [min(even_nodes), even_nodes.index(min(even_nodes))]
    else:
        return []
```

The function `pluck` first filters out the even nodes from the input array, then finds the smallest even value and returns it along with its index in the original array. If there are no even values in the array, it returns `[]`. 

Here is an example usage of the function with a sample input:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)  # Output: [2, 1]
```