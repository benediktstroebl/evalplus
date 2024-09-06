```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and the product of their signs before returning the result. Magnitudes are summed up, and signs are computed and multiplied together using the `prod` function. The resulting outcome is obtained by multiplying the sum of magnitudes by the product of signs. If the array is empty, the function returns `None`.

Here's an example usage:
```python
prod_signs([1, 2, 2, -4]) # -9
prod_signs([0, 1]) # 0
prod_signs([]) # None
```
The function matches the expected outputs for the given examples in the markdown code block.