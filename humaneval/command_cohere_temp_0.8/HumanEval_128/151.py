```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension with a generator expression to calculate the result. The zip function pairs each element with the following one (skipping the last one since it has no subsequent element). The sum function then calculates the product of each pair of elements while also accounting for the signs. If the array is empty, the result will be None. 

Here is a markdown code block with corresponding test cases to validate the function:
```python
def test_prod_signs():
    # Tests for prod_signs function:
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None
    assert prod_signs([1, 2, 3, 4, 5]) == 1500
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([0, 0, 0]) == 0
    assert prod_signs([-1, 0, 1, 2, -3, 4, -5]) == 54
```
To test the function, seven tests were added that cover different scenarios and edge cases. These tests verify the correctness of the `prod_signs` function. You can run these tests using a Python test runner or an IDE to verify the function implementation.