```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm works by the Euclidean algorithm concept, which states that the gcd of two numbers `(a, b)` is the same as the gcd of `b % a` and `a`. In the case where `a` is 0, it returns `b` because `b` would be the gcd of `0` and any other number. 

Here is a test suite for this function:
```python
def test_gcd():
    """
    Tests the greatest_common_divisor function.
    """
    assert greatest_common_divisor(4, 2) == 2
    assert greatest_common_divisor(0, 180) == 0
    assert greatest_common_divisor(78, 10) == 2
    assert greatest_common_divisor(121, 26) == 13
    assert greatest_common_divisor(121, 0) == 121
```
This test suite contains several test cases that cover different scenarios and edge cases for the `greatest_common_divisor` function. Each test case verifies that the function returns the expected output for a given input.

To run the test suite, you can use a test runner like Pytest, or you can run it directly in your Python environment. Here is an example of executing the test file:
```python
python -m pytest -vv test_gcd.py
```

This will run the test suite and display detailed information about each test, including the names of the tests, whether they passed or failed, and any relevant error messages. The `-vv` option increases the verbosity of the test results, providing more information during testing.

Make sure to have the `pytest` package installed in your Python environment, if not, you can do it with:
```bash
pip install pytest
```
This will install the `pytest` package and allow you to run the test suite.  In this way, you can ensure that the `greatest_common_divisor` function behaves as expected and is correct.  The `assert` statements within the test cases check if the actual output of the function is equal to the expected output.  If the actual output matches the expected output, the test case will pass, and if they are different, the test case will fail, generating an error message.  This approach allows to detect if there is any bug or unexpected behavior in the function.  The `test_gcd()` function is a very basic example of test cases, but they provide a good starting point to ensure the correctness of the `greatest_common_divisor` function and catch potential issues.  By running these tests regularly, you can have confidence in the reliability and accuracy of the function.  If you want to implement other test cases or specific scenarios, you can easily add them to this test suite to cover a more comprehensive set of input and output scenarios.  This allows you to ensure that the function works correctly for a variety of inputs, including edge cases and boundary conditions.  This approach to testing is crucial to ensure the correctness of your code and helps to catch potential errors or unexpected behaviors before deploying your code in a production environment.  Testing is an important part of software development, and writing tests for your code helps to ensure its quality, reliability, and robustness.  In addition, this approach adheres to the principles of test-driven development(TDD), which is a software development process