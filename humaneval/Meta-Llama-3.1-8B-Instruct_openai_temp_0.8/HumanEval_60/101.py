```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the sum.

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
    return sum(range(1, n + 1))


# Test the function
if __name__ == "__main__":
    print(sum_to_n(30))
    print(sum_to_n(100))
    print(sum_to_n(5))
    print(sum_to_n(10))
    print(sum_to_n(1))
```

This script defines a function called `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses Python's built-in `sum` function in combination with the `range` function to achieve this.

The `range` function generates a sequence of numbers from 1 to `n`, and the `sum` function adds up these numbers. The `+ 1` in `range(1, n + 1)` ensures that `n` is included in the sequence, so that the function returns the correct result even when `n` is equal to 1.

The script also includes some test cases to verify that the function works correctly. The `if __name__ == "__main__":` block ensures that the test cases are only executed when the script is run directly (i.e., not when it is imported as a module by another script).