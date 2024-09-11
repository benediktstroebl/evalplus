```python
def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the summation.

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
    # Calculate the sum using the formula for the sum of an arithmetic series
    # The formula is n * (a1 + an) / 2, where a1 is the first term and an is the last term
    # In this case, a1 is 1 and an is n
    return n * (1 + n) // 2


# Test cases
print(sum_to_n(30))   # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

This script defines the `sum_to_n` function that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the formula for the sum of an arithmetic series to calculate the sum. The script then includes some test cases to demonstrate the function's behavior.