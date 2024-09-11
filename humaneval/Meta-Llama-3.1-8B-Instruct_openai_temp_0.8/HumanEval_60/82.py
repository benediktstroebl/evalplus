```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    return (n * (n + 1)) // 2

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script uses the formula for the sum of an arithmetic series (`n * (n + 1) / 2`) to calculate the sum of numbers from 1 to `n`. This approach is more efficient than a naive loop-based solution, especially for large values of `n`.