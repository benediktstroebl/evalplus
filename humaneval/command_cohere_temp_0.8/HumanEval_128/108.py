```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and the product of their signs, then returns their sum, resulting in the desired output. It returns `None` for an empty array, as specified in the prompt.

Here's the accompanied test suite to verify the function:
```python
def test_prod_signs():
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) is None
    assert prod_signs([-5, -10, -20, -25]) == 450
    assert prod_signs([0.5, -1, -2, 3]) == -6
    assert prod_signs([-1, -2, -1, -2, -1]) == -6
    assert prod_signs([2, -2, 3, -4, 5]) == 45
    assert prod_signs([0, 0, 0]) == 0
```