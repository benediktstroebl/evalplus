```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of numbers from 1 to n.

    Example:
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
        raise ValueError("Input number must be greater than 0")

    return n * (n + 1) // 2

# Test the function
if __name__ == "__main__":
    test_cases = [30, 100, 5, 10, 1]
    for n in test_cases:
        try:
            result = sum_to_n(n)
            print(f"Sum of numbers from 1 to {n}: {result}")
        except ValueError as e:
            print(e)
```

This Python script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula for the sum of an arithmetic series: `n * (n + 1) / 2`. The script also includes a test suite to verify the correctness of the function. If the input number is less than 1, the function raises a `ValueError` with a message indicating that the input number must be greater than 0.