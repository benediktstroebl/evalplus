```python
# sum_to_n.py

def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.
    
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
    return (n * (n + 1)) // 2


# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

In this script, the `sum_to_n` function takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The `doctest` module is used to test the function with the provided examples. To run the tests, save the script and execute it with `python sum_to_n.py`.