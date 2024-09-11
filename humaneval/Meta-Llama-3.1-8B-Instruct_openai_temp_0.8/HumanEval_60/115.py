```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n using the arithmetic series formula (n*(n+1))/2.

    Args:
        n (int): The upper limit of the series.

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

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

In this script, we define a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the arithmetic series formula. This formula is derived from the formula for the sum of an arithmetic series: `S = n/2 * (a + l)`, where `S` is the sum of the series, `n` is the number of terms, `a` is the first term, and `l` is the last term. In this case, `a = 1` and `l = n`, so we get `S = n/2 * (1 + n) = n * (n + 1) / 2`. This formula is much more efficient than iterating over all the numbers from 1 to `n`, especially for large values of `n`.

The function is well-documented with a docstring that explains its purpose, arguments, return value, and provides examples of usage. We also include some test cases to demonstrate the function's behavior.