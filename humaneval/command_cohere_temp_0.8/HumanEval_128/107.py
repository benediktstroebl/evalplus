```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension that multiplies corresponding elements with signs represented by 1, -1 or 0, and then sums them up. The outcome is returned as None if the list is empty.

Here is a test suite that can be used to validate the function:
```python
def test_prod_signs():
    # Example 1
    assert prod_signs([1, 2, 2, -4]) == -9
    # Example 2
    assert prod_signs([0, 1]) == 0
    # Edge Case
    assert prod_signs([]) is None
    # Negative Numbers
    assert prod_signs([-2, 2, -3, 3]) == -6
    # Mixed Signs
    assert prod_signs([2, -2, 2, -2, 2]) == -8
    # Numbers with 0 Sign
    assert prod_signs([2, 0, 2, -2]) == 0
```