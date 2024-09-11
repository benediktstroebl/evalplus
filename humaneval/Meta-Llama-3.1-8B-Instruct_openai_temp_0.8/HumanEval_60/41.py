```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit for the sum.

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
    # Use the formula n*(n+1)//2 to calculate the sum
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Should print 465
print(sum_to_n(100))  # Should print 5050
print(sum_to_n(5))  # Should print 15
print(sum_to_n(10))  # Should print 55
print(sum_to_n(1))  # Should print 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula `n*(n+1)//2`. The formula is implemented in the function body, and it's the most efficient way to calculate the sum. The script also includes some test cases at the end to verify that the function is working correctly.