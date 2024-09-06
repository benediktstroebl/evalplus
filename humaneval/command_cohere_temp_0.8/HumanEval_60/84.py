```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): The highest number to be included in the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers

# Testing the function with different inputs
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

This script defines a function `sum_to_n`, which calculates the sum of numbers from 1 to `n` using the sum formula for the first n natural numbers. The function takes an integer `n` as an argument and returns the corresponding sum.

The code includes a testing section where the function is tested with different inputs to ensure it behaves as expected. The ">>>" symbol is used to represent the output of the function when printed, and the expected output is provided in parentheses for each case.