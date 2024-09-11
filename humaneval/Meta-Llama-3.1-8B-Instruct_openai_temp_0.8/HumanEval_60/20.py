```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n using the formula for the sum of an arithmetic series.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    int: The sum of numbers from 1 to n.

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
    # The formula for the sum of an arithmetic series is: n * (a1 + an) / 2
    # where n is the number of terms, a1 is the first term, and an is the last term
    # Since we're summing numbers from 1 to n, a1 = 1 and an = n
    # The number of terms is also n, so the formula simplifies to: n * (1 + n) / 2
    return n * (1 + n) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula for the sum of an arithmetic series. It then tests this function with the provided test cases. Note that I used integer division (//) to ensure the result is an integer.