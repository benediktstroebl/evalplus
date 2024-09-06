```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the sign of each number in the array and stores them in the `signs` list. Finally, it returns the sum of the magnitudes multiplied by the product of all signs, which is computed using the `prod()` function.

Here is an example usage of the function:
```python
arr = [1, 2, 2, -4]
print(prod_signs(arr))  # -9
```
This will return `-9` as the result, since the magnitude of the array is `[1, 2, 2, 4]`, the signs are [1, 1, 1, -1], and the sum of magnitudes is `10` while the product of signs is `-1 * 1 * 1 * -1 = -9`.