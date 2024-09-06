```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function follows the specifications as it returns None for an empty array, and for non-empty arrays, it calculates the product of all signs of each number in the array and the sum of magnitudes of integers, and returns their product. 

The product of all signs and the sum of magnitudes are calculated using Python's built-in functions prod and sum respectively, and the result is returned as their product.

This solution allows for arrays containing negative, zero, and positive values, and handles an empty array appropriately.