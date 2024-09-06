```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and product of all signs of each number in the array and returns their product. The result is `None` for an empty array.

Here is a breakdown of the code:
1. `result = None`: Initializes the result to `None` to denote an empty input array.
2. `if arr`: Checks if the input array `arr` is not empty.
3. `magnitudes = [abs(x) for x in arr]`: Calculates the magnitudes of each integer in the array.
4. `signs = [x > 0 for x in arr]`: Determines the signs of each number in the array.
5. `result = sum(magnitudes) * prod(signs)`: Multiplies the product of the signs by the sum of magnitudes.
6. Returns the result. 

This solution is test-driven and can be implemented using Python as a standalone function.