```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the sum (inclusive).
    
    Returns:
    int: The sum of numbers from 1 to n.
    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Calculate the sum using the formula for the sum of an arithmetic series
    total = n * (n + 1) // 2
    
    return total

# Test cases
print(sum_to_n(30))   # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))    # Expected output: 15
print(sum_to_n(10))   # Expected output: 55
print(sum_to_n(1))    # Expected output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the formula for the sum of an arithmetic series, `n * (n + 1) / 2`, to calculate the sum. The script also includes test cases to verify the function's correctness. If the input `n` is not a positive integer, the function raises a `ValueError`.