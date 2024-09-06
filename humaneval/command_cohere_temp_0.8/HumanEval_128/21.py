```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function performs the multiplication of pairs of successive elements in the list, taking into account their signs, and returns the sum of these products. If the array is empty, it returns None.