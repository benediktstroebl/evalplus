```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the signs of each number in the array and stores them in the `signs` list. Subsequently, it returns the sum of the magnitudes multiplied by the product of all signs, represented by 1, -1, or 0, to obtain the final result.

The `prod_signs` function returns `None` for an empty array, as specified in the problem statement.

The following would be an example of how to test this function:
```python
prod_signs([1, 2, 2, -4])  # Expected: -9
prod_signs([0, 1])  # Expected: 0
prod_signs([])  # Expected: None
```
These tests evaluate the `prod_signs` function with three distinct cases and verify if the returned result matches the expected outcome.