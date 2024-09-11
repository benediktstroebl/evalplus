```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit for the sum.

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
    # Validate the input to ensure it's a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    # Calculate the sum using the formula for the sum of an arithmetic series
    return (n * (n + 1)) // 2

# Test the function with some examples
print(sum_to_n(30))   # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))    # 15
print(sum_to_n(10))   # 55
print(sum_to_n(1))    # 1
```

In this script, we define the `sum_to_n` function that takes a positive integer `n` as input and returns the sum of numbers from 1 to `n`. We use the formula for the sum of an arithmetic series to calculate the sum efficiently. The function includes input validation to ensure that the input is a positive integer. Finally, we test the function with the provided examples.