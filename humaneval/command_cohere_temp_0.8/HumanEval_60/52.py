```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This Python script defines a function called sum_to_n, which takes an integer n as input and returns the sum of integers from 1 to n. The function uses the sum function to calculate the sum of the range from 1 to n, inclusive. 

To test this function, you can write a few corresponding tests that verify its behavior:
```python
# Test case with positive integer input
assert sum_to_n(5) == 15, "sum should be 15 for input 5"

# Test case with input exceeding 100
assert sum_to_n(105) == 5500, "sum should be 5500 for input 105"

# Test case with single-digit input
assert sum_to_n(2) == 3, "sum should be 3 for input 2"

# Test case with zero input
assert sum_to_n(0) == 0, "sum should be 0 for input 0"
```

This code provides five test cases that aim to evaluate the correctness of the `sum_to_n` function. Each assert statement checks if the output of the function is equal to the expected value. If the condition is true, the test passes, confirming the function's expected behavior. If the condition is false, the test fails, indicating a mismatch between the function's output and the expected result.

This way, the sum_to_n function is tested against various input scenarios to ensure that it properly computes the sum of integers from 1 to 'n'.