```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension with a generator expression to calculate the multiplication of each number's sign. The result is then returned from the function. In the case of an empty array, None is returned. This approach ensures efficiency and readability.