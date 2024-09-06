```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    Note: this sums upwards to n."""
    return n * (n + 1) // 2  # Sum of integers up to n is n * (n+1) / 2
```

This function utilizes a simple formula to compute the sum of integers from 1 to `n` as `n * (n + 1) / 2`. This expression simplifies to `n * (n + 1) / 2` for integer addition, providing a more intuitive explanation of the operation, while remaining accurate to the problem description.

To validate this function, you can write a test suite that includes the provided test cases from the original problem statement:
```python
# Test the sum_to_n function
def test_sum_to_n():
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1
```

Executing these test cases ensures the function provides the expected results for different input values.