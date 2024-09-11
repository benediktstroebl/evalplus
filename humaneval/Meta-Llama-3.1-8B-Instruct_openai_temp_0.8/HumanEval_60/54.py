```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Example:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
    """
    return (n * (n + 1)) // 2


# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula `n * (n + 1) // 2`. This formula is derived from the fact that the sum of an arithmetic series is the average of the first and last term, multiplied by the number of terms. The `//` operator is used for integer division to ensure that the result is an integer. The script also includes test cases to verify the correctness of the function.