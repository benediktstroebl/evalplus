```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This Python script defines a function called sum_to_n, which takes an integer n as input and returns the sum of integers from 1 to n. The function uses the sum function to calculate the sum of the range from 1 to n, inclusive. 

To test this function, you can write a few corresponding tests that verify the correctness of the function:
```python
# Test sum_to_n with input 30
assert sum_to_n(30) == 465

# Test sum_to_n with input 100
assert sum_to_n(100) == 5050

# Test sum_to_n with input 5
assert sum_to_n(5) == 15

# Test sum_to_n with input 10
assert sum_to_n(10) == 55

# Test sum_to_n with input 1
assert sum_to_n(1) == 1
```

All tests are intended to verify the correctness of the sum_to_n function, ensuring that it produces the expected results for a variety of inputs.

You can run these tests individually with the python command to verify the correctness of the function and to ensure that the function behaves as expected. 

This approach provides a comprehensive suite of tests to validate the functionality of the sum_to_n function and ensures that it complies with the problem statement.