```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the input array and assigns them to the `magnitudes` list, it also determines the signs of the integers and assigns them to the `signs` list. The function then calculates the product of the signs and the sum of the magnitudes, resulting in the desired output. If the input array is empty, it returns `None`.

Here's the detailed explanation of the code:
1. The `prod_signs` function takes one parameter `arr`, which is the input array of integers.
2. The first line inside the function checks if the `arr` is empty. If it is empty, the function will return `None`, as specified in the problem statement.
3. If the array is not empty, it contains integers to work with, so the remainder of the code executes.
4. The `magnitudes` list comprehension is used to calculate the absolute value of each integer in the array `arr`. The `abs()` function is applied to each element in the list, resulting in a list of magnitudes.
5. Similarly, the `signs` list comprehension is used to determine the sign of each integer in the array `arr`. It checks if each integer is greater than or equal to zero, assigning a value of `1` to indicate a positive sign, if the integer is less than zero it assigns `-1` to indicate a negative sign, and if the integer is exactly zero, it assigns `0` to the `signs` list.
6. The next line calculates the sum of the magnitudes multiplied by the product of the signs. The `prod()` function flattens the `signs` list and multiplies its elements together. This result is then multiplied by the sum of the magnitudes calculated earlier.
7. Finally, the function returns the computed value that answers the problem statement.

This solution adheres to the problem's requirement of returning `None` for an empty array, and efficiently computes the correct result for a non-empty array.