```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and product of all signs of each number in the array and returns their product. It returns `None` for an empty array.

Here's how the function works step by step:
1. `result = None`: Initializes the result to `None` so that it can be updated later.
2. `if arr`: Checks if the input array `arr` is not empty.
3. `magnitudes = [abs(x) for x in arr]`: Calculates the magnitudes of each integer in the array by using the `abs()` function. This value is a list.
4. `signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]`: Calculates the signs of each integer in the array. If a number is positive, it assigns `1`; if negative, it assigns `-1`; and if it's zero, it assigns `0`. This results in a list of signs.
5. `result = sum(magnitudes) * prod(signs)`: Calculates the final result by multiplying the sum of magnitudes (`sum(magnitudes)`) by the product of signs (`prod(signs)`).
6. Returns `result`: Returns the final result.

The `prod()` function is used to calculate the product of a list of numbers. In Python, the `prod()` function returns `1` if the list is empty, and this is why initially the result is set to `None` to account for the case when the array is empty and finally return `None` in this case.

This solution follows the specification of the problem as it returns `None` for an empty array and calculates the correct value for non-empty arrays.