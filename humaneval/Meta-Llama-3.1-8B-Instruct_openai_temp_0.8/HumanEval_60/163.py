```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

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
    if n <= 0:
        return 0  # If n is not positive, the sum is 0
    return n + sum_to_n(n - 1)  # Recursive formula for sum of numbers

# Alternatively, you can also use a more efficient iterative approach
def sum_to_n_iterative(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n_iterative(30)
        465
        >>> sum_to_n_iterative(100)
        5050
        >>> sum_to_n_iterative(5)
        15
        >>> sum_to_n_iterative(10)
        55
        >>> sum_to_n_iterative(1)
        1
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Test the functions
print(sum_to_n(30))
print(sum_to_n_iterative(30))
```

The `sum_to_n` function uses a recursive approach to calculate the sum, while the `sum_to_n_iterative` function uses an iterative approach with a for loop. Both functions have the same time complexity of O(n), but the iterative approach is generally more efficient in practice due to the overhead of recursive function calls.