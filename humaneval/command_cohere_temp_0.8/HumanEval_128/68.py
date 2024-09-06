```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the input array and identifies their signs, assigning 1 to positive numbers, -1 to negative numbers, and 0 to zero. It then calculates the sum of the magnitudes and the product of the signs before returning the final result.

Here is an example usage:
```python
prod_signs([1, 2, 2, -4]) # -9
prod_signs([0, 1]) # 0
prod_signs([]) # None
```
Which aligns with the examples provided in the problem description.