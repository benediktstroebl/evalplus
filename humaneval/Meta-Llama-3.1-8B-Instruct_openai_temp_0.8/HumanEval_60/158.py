```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n using the formula for the sum of an arithmetic series.

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
    # The formula for the sum of an arithmetic series is n * (a1 + an) / 2, 
    # where n is the number of terms, a1 is the first term, and an is the last term.
    # In this case, the number of terms is n, the first term is 1, and the last term is n.
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))   # prints 465
print(sum_to_n(100))  # prints 5050
print(sum_to_n(5))    # prints 15
print(sum_to_n(10))   # prints 55
print(sum_to_n(1))    # prints 1
```

This script uses the formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to n. The formula is n * (a1 + an) / 2, where n is the number of terms, a1 is the first term, and an is the last term. In this case, the number of terms is n, the first term is 1, and the last term is n. This makes the formula n * (1 + n) / 2, which is simplified to n * (n + 1) / 2.