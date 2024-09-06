```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(num) for num in arr) * product(num > 0, num < 0, num == 0 for num in arr)
    return result
```
This function calculates the magnitude of each number in the array using a generator expression, then uses the `product()` function to multiply the signs together, and finally returns the sum of the magnitudes multiplied by the product of the signs.

Here is a markdown code block with tests for the given problem:
```python
def test_prod_signs():
    # None for empty arr
    assert prod_signs([]) is None
    assert prod_signs([0, 1]) == 0
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([-3, -1, -1, 1, 1]) == -6
    assert prod_signs([2, -2, -2, 2]) == -8  # mixed sign
    assert prod_signs([0]) == 0
    assert prod_signs([2, 3, -4, 0, 6]) == 54

test_prod_signs()
```
This will verify the correctness of the `prod_signs` function.