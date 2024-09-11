### Summing Numbers from 1 to n

Here's a self-contained Python script that uses the mathematical formula for the sum of an arithmetic series to efficiently calculate the sum of numbers from 1 to n.

```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    
    Examples:
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
    return n * (n + 1) // 2

# Example usage:
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script uses the mathematical formula for the sum of an arithmetic series, which is `n * (n + 1) / 2`, to calculate the sum of numbers from 1 to n. The `//` operator is used for integer division to ensure the result is an integer.

This approach is more efficient than using a loop to sum the numbers from 1 to n, especially for large values of n.