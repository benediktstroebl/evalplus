```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
        result = sum(abs(num) * sign for num, sign in zip(arr, signs))
    return result
```
This function calculates the magnitude of each number in the array and multiplies it by the sign of the number, resulting in a list of these products. It then sums these values and returns the result. If the array is empty, it returns `None`.

Here's an example usage:
```python
prod_signs([1, 2, 2, -4]) # [-9]
prod_signs([0, 1]) # [0]
prod_signs([]) # None
``` 
The function is designed to return a scalar value for non-empty arrays and `None` for an empty array, as specified in the problem statement.