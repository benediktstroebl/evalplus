```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the input array and determines their signs, assigning each sign a value of 1, -1, or 0. It then calculates the sum of the magnitudes and the product of the signs, multiplying these two values to obtain the desired result. If the input array is empty, the function returns None.

Here's an example usage:
```python
prod_signs([1, 2, 2, -4]) # Output: -9
prod_signs([0, 1]) # Output: 0
prod_signs([]) # Output: None
```
The function will calculate the required result based on the given input and return it in the corresponding unit (integer or None).