```python
def sum_to_n(n: int):
    """
    This function calculates the sum of all numbers from 1 to n.

    Parameters:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of all numbers from 1 to n.

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

# Test the function with the provided examples
print(sum_to_n(30))  
print(sum_to_n(100))
print(sum_to_n(5))  
print(sum_to_n(10))
print(sum_to_n(1))
```

This script defines a function `sum_to_n` that takes an integer `n` as input, calculates the sum of all numbers from 1 to `n` using the built-in `sum` and `range` functions, and returns the result. The script then calls the function with the provided example inputs and prints the results.