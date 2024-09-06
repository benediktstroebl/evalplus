```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension to multiply each number in the array by the following number's sign, and then sums these products to calculate the result, setting it to None for an empty array.

Here is a test suite that you can use to test this solution:
```python
def test_prod_signs():
    # Positive test cases
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([2, -2, 1, -1]) == -2

    # Edge case
    assert prod_signs([0]) == None

    # Negative test case
    assert prod_signs([1, 2, -1]) == -2
```
You can then run the test_prod_signs function to verify the correctness of the solution.

This problem can be solved in different ways, this solution uses list comprehension and zip to multiply and sum in the same operation, but it doesn't matter how it is solved as long as it conforms to the problem statement.