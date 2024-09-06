```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This Python script defines a function called sum_to_n, which takes an integer n as input and returns the sum of integers from 1 to n. The function uses the sum function to calculate the sum of the range from 1 to n, inclusive. 

To test this function, you can write a markdown code block with a few test cases to ensure it behaves as expected:
```python
def test_sum_to_n():
    """Tests for sum_to_n function."""
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1
```

In the test_sum_to_n function, the assert statements will raise an AssertionError with an error message if the condition fails, indicating that the function does not behave as expected.  If you run this code using a Python test runner, such as pytest or unittest, it will automatically discover and run this test module.

To run this test suite, you can use a testing framework like pytest:
```bash
pytest -v
```
This command will execute the test suite and display test results, including any failed tests and error messages. 
If all tests pass, you will see an output message indicating that all tests were successful. In this way, you can confidently confirm that the sum_to_n function works correctly.  If the tests fail, it provides an indication of where things went wrong, aiding in debugging the function. 

This systematic approach of writing tests first helps you ensure the correctness of your code and provides a safety net when making changes in the future.  You can add more tests to this suite to cover a diverse range of scenarios, providing even more confidence in the function's correctness.