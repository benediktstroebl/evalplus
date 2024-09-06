```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array and the product of the signs and returns the sum of the magnitudes multiplied by the product of the signs. The result is None for an empty array.

Here is a Markdown code block with corresponding test cases to verify the correct operation of the function:
```python
def test_prod_signs():
    # Test case 1
    input1 = [1, 2, 2, -4]
    expected1 = -9
    result1 = prod_signs(input1)
    assert result1 == expected1

    # Test case 2
    input2 = [0, 1]
    expected2 = 0
    result2 = prod_signs(input2)
    assert result2 == expected2

    # Test case 3
    input3 = []
    expected3 = None
    result3 = prod_signs(input3)
    assert result3 == expected3

test_prod_signs()
```
This test suite will verify that the `prod_signs` function operates correctly for the provided examples from the problem statement.