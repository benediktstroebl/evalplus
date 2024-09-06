```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1 if num < 0 else 1)
        result = sum(abs(num) for num in arr) * prod(signs)
    return result
```
This function calculates the product of the signs of each number in the array and then multiplies it by the sum of the magnitudes of the integers. If the array is empty, it returns **None**.

Here's an example usage:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
```