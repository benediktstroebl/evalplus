Here's a Python script with a self-contained function `generate_even_digits()` that solves the problem:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    # Ensure a is the smallest number
    if a > b:
        a, b = b, a
        
    even_digits = [x for x in range(a, b + 1, 2)]
    
    return even_digits

# Testing the function
def test_even_digits():
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == []

test_even_digits()
```

This script includes the function `generate_even_digits()` and a test function `test_even_digits()` that verifies the correctness of the solution. 

The test is invoked at the end of the script to ensure that the function works correctly. If the test passes, the script output will be empty; otherwise, it will display the test failures.