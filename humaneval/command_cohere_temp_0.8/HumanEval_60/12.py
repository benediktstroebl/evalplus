```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Number of integers to sum.
        
    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers

# Testing the function with doctests
def test_sum_to_n():
    """Tests the sum_to_n function."""
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1
```

The provided code defines a Python function called `sum_to_n` that calculates the sum of the first 'n' integers. It uses the formula '(n)(n+1)/2' to compute this sum, which is the sum of the first 'n' natural numbers. The function is equipped with docstrings and doctests, a combination of descriptive text and embedded test cases to illustrate its usage and validate its correctness. The accompanying `test_sum_to_n` function checks the `sum_to_n` function against these test cases and asserts that it behaves as expected, returning the correct sums for various values of 'n'.