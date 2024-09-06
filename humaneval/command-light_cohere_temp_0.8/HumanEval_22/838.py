Here is a self-contained Python function that filters integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 'three', (])
values2 = [3.14, 5, 'four', (1, 2)]

print(filter_integers(values1))  # Output: [1, 2, 'three']
print(filter_integers(values2))  # Output: [3.14, 5, 'four', (1, 2)]
```

The function uses the `isinstance` built-in function to check if each element in the input list is an integer. The function then returns a list containing only the integers from the original list.