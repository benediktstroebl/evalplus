Here's a Python script that includes a self-contained function designed to solve the problem presented:
```python
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes:
        min_value = min(even_nodes)
        min_index = even_nodes.index(min_value)
        return [min_value, min_index]
    else:
        return []
```

This function identifies even nodes using a list comprehension and utilizes the `min` function to determine the smallest even value. The `index` method is used to find the index of the smallest even value. Ultimately, the function returns a list containing the smallest even value and its corresponding index.

Here's an example of how you can use the function and illustrate its behavior:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)
```

For the given example, the output would be:
```
[2, 1]
```

This demonstrates the function's capability to identify the smallest even value (2) and its index (1) from the array.