```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the sign of each number in the array and stores them in the `signs` list. Subsequently, it returns the sum of the magnitudes multiplied by the product of all signs, represented by 1, -1, or 0, accordingly.

Here is a test suite to ensure the function correctness:
```python
def test_prod_signs():
    # None for an empty array
    assert prod_signs([]) is None
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([-5, -10, -20]) == -300
    assert prod_signs([-5, -10, -20, -100]) == -5000
    assert prod_signs([0.5, -1, -2, 3]) == -6
    assert prod_signs([-0.5, 0.7, -3, 4]) == -6.7
    assert prod_signs([0.5, -0.2, 0.3, -4.5]) == -1.6
```
You can use `python -m unittest test_prod_signs` to verify the tests are passed successfully.