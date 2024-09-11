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
    return sum(range(1, n + 1))

# Alternatively, you can use a mathematical formula to calculate the sum in O(1) time
def sum_to_n_formula(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n using the formula n*(n+1)/2.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n_formula(30)
        465
        >>> sum_to_n_formula(100)
        5050
        >>> sum_to_n_formula(5)
        15
        >>> sum_to_n_formula(10)
        55
        >>> sum_to_n_formula(1)
        1
    """
    return n * (n + 1) // 2

print(sum_to_n(30))  # Output: 465
print(sum_to_n_formula(30))  # Output: 465
```

This script defines two functions: `sum_to_n` and `sum_to_n_formula`. The `sum_to_n` function uses the built-in `sum` function with the `range` function to calculate the sum of numbers from 1 to n. The `sum_to_n_formula` function uses the mathematical formula `n*(n+1)/2` to calculate the sum in O(1) time. The script also includes some example use cases and prints the results of both functions for n=30.