```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Use the mathematical formula for the sum of an arithmetic series
    # to calculate the sum without using a loop
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines the `sum_to_n` function, which uses the mathematical formula for the sum of an arithmetic series to efficiently calculate the sum of numbers from 1 to `n`. The function is then tested with various inputs to verify its correctness.