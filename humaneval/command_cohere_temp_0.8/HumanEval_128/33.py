```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        product_of_signs = prod(signs)
        result = sum(magnitudes) * product_of_signs
    return result
```
This function `prod_signs()` takes an array `arr` as an argument, and returns the sum of magnitudes of integers multiplied by product of all signs of each number in the array. The function checks if the array is empty, and returns `None` if so. Otherwise, it calculates the magnitude of each number and the product of signs, then multiplies them together and returns the result.