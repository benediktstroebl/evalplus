```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array and the product of the signs and then returns their sum, yielding the desired result.

Here are some example inputs and expected outputs to explain the function:
1. ```prod_signs([1, 2, 2, -4]) == -9```
2. ```prod_signs([0, 1]) == 0```
3. ```prod_signs([]) == None```

The function prod_signs handles an empty array by returning None, as specified in the prompt.