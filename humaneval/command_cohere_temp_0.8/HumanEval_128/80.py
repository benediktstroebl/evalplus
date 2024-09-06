```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the signs of each number in the array and stores them in the `signs` list. Subsequently, it returns the sum of the magnitudes multiplied by the product of all signs, represented by 1, -1, or 0, accordingly.

Here is a self-contained Python script that includes corresponding tests for the function `prod_signs()` using pytest:
```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result

def test_prod_signs():
    # Test case 1
    input1 = [1, 2, 2, -4]
    expected1 = -9
    result = prod_signs(input1)
    assert result == expected1

    # Test case 2
    input2 = [0, 1]
    expected2 = 0
    result = prod_signs(input2)
    assert result == expected2

    # Test case 3
    input3 = []
    expected3 = None
    result = prod_signs(input3)
    assert result == expected3

if __name__ == "__main__":
    test_prod_signs()
```
This script utilizes the `pytest` framework, an automated testing tool for Python, to test the function `prod_signs()`. Specifically, it implements three test cases, each of which involves passing an input array and expecting a particular output. The `assert` statements are used to verify that the actual output from the function matches the expected output for each test case. If all assertions pass successfully, you will see the output stating that many tests have been completed successfully indicating that the function `prod_signs()` operates as expected. 

Note that this Python script is test-driven, meaning it focuses on creating tests to validate the correctness of the code before writing the actual function. This approach helps to ensure that the code meets the desired requirements and behaves correctly. Test-driven development can also serve as a documentation tool, making the code more readable and easier to maintain or modify in the future.  Assuming you have python installed you can run this script by copying it and executing it in your terminal  and it will execute the tests inside accordingly.