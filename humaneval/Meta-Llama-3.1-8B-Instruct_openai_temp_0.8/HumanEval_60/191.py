```python
# This script provides a function to calculate the sum of numbers from 1 to n.

def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
    n (int): The upper limit of the range of numbers to sum.

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
    if n < 1:
        return "Input must be a positive integer."
    return n * (n + 1) // 2

# Testing the function
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This script provides a simple function, `sum_to_n`, that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the mathematical formula for the sum of an arithmetic series, which is `n * (n + 1) / 2`. If the input is not a positive integer, the function returns an error message.