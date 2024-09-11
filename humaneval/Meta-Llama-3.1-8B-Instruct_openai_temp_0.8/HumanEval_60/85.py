```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    # Use the formula for the sum of an arithmetic series: n(n + 1) / 2
    return n * (n + 1) // 2

# Example usage:
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the formula for the sum of an arithmetic series: `n(n + 1) / 2`. The function also includes input validation to ensure that `n` is a non-negative integer. If `n` is not a non-negative integer, the function raises a `ValueError`.