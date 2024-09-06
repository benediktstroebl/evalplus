```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): The highest number to be included in the sum.
        
    Returns:
        int: The sum of integers from 1 to n (inclusive).
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers

# Testing the function with doctests
import doctest

def test_sum_to_n():
    """Test the sum_to_n function by checking if it returns correct sums for various inputs."""
    doctest.testmod(verbose=True)
```

To test the function, the script employs the `doctest` module, incorporating test cases into the function's docstring. When the `testmod` function is called, it runs these tests, confirming that the `sum_to_n` function operates as expected. Adjust the `verbose=True` parameter to see detailed test results.

Ensure that you run this script in a Python environment that includes the `doctest` module (typically, the standard library). If `doctest` is not available, you can manually add test cases and assertions to validate the function.