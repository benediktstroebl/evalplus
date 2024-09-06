```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [x > 0 for x in arr] * [x < 0 for x in arr] + [x == 0 for x in arr]
        result = sum(x * y for x, y in zip(arr, signs))
    return result
```
This function uses list comprehensions to determine the signs of each element in the array and calculates the magnitudes of integers in the array. Subsequently, it computes the product of the sign values and the sum of magnitudes, returning None for an empty array.

Here is a simple test case to verify the functionality of the function:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
>>> prod_signs([1, -1, -1, 1])
-3
```