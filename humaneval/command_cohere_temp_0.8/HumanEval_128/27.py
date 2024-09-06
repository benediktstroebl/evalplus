```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1)
        signs *= [num < 0 for num in arr]
        result = sum([num for num in arr]) * prod(signs)
    return result
```
This function calculates the product of all signs of each number in the array, represented by 1, -1, or 0, and then multiplies it by the sum of magnitudes of integers in the array. The result is returned if the array is not empty, and `None` is returned otherwise.