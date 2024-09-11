```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The number up to which the sum is calculated.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Using the formula for the sum of an arithmetic series
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that uses the formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to `n`. The formula is `n * (n + 1) // 2`, which is more efficient than calculating the sum iteratively. The script then includes test cases to verify the function's correctness.