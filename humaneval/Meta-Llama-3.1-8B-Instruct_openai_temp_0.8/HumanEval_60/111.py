```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
        n (int): The input number up to which the sum is calculated.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Use the formula n * (n + 1) // 2 to calculate the sum efficiently
    # This formula is derived from the formula for the sum of an arithmetic series
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n`. It uses the formula `n * (n + 1) // 2` to calculate the sum efficiently. The function also includes input validation to ensure that `n` is a positive integer. The script includes test cases to verify the correctness of the function.