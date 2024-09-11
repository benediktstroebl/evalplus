```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit for the sum.

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
    # Using the arithmetic series formula: n*(n+1)/2
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))  # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))  # 1
```

Note: This solution uses the arithmetic series formula `n*(n+1)/2`, which is more efficient than summing numbers from 1 to n in a loop, especially for large values of n.