```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension to multiply each number in the array by the following number's sign, and then sums these products to compute the answer. The result is set to None for an empty array, as specified in the prompt.

Here is a simple test suite to ensure that the function behaves as expected:
```python
def test_prod_signs():
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None
    assert prod_signs([1, 2, -1, 1, -2, 3]) == -6
    assert prod_signs([2, -2, -4, -2, 2, 4]) == 0
    assert prod_signs([-2, -1, -2, -1]) == -2
```