```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function works by multiplying subsequent elements in the array together, taking into account their signs. It then sums these products together to form the final result.