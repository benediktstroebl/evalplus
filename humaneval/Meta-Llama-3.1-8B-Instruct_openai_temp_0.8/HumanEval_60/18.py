### Summing Numbers from 1 to n
#### Overview
This script provides a function `sum_to_n` that calculates the sum of numbers from 1 to a given number `n`.

#### Code
```python
def sum_to_n(n: int) -> int:
    """
    Sums numbers from 1 to n.

    Args:
    n: A positive integer.

    Returns:
    The sum of numbers from 1 to n.

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
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Use the formula for the sum of an arithmetic series
    # The formula is n * (a1 + an) / 2, where a1 is the first term (1) and an is the last term (n)
    return n * (1 + n) // 2

# Test the function
print(sum_to_n(30))  # Should print 465
print(sum_to_n(100))  # Should print 5050
print(sum_to_n(5))  # Should print 15
print(sum_to_n(10))  # Should print 55
print(sum_to_n(1))  # Should print 1
```

#### Explanation
The function `sum_to_n` takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the formula for the sum of an arithmetic series, which is `n * (a1 + an) / 2`, where `a1` is the first term and `an` is the last term. The function first checks if `n` is a positive integer, and raises a `ValueError` if it is not. Then it calculates the sum using the formula and returns the result. The test cases at the end of the script demonstrate the function's behavior.