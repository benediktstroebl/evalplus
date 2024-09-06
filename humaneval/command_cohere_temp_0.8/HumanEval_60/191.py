```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Test suite
def test_sum_to_n():
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1

# Run the tests when the script is directly executed
if __name__ == "__main__":
    test_sum_to_n()
```

The function `sum_to_n` uses the sum formula for the first n natural numbers, which is `n(n + 1) / 2`. This works for any positive integer `n`, giving the correct sum from 1 to n. Test cases are included to validate the function for different values of `n`.