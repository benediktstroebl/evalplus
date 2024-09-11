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
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    # We use the formula for the sum of an arithmetic series: n * (n + 1) // 2
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1

# Test the function with invalid input
try:
    print(sum_to_n(-5))
except ValueError as e:
    print(e)  # Output: Input must be a positive integer

try:
    print(sum_to_n(3.5))
except ValueError as e:
    print(e)  # Output: Input must be a positive integer
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the formula for the sum of an arithmetic series, which is more efficient than using a loop to calculate the sum. The function also includes input validation to ensure that `n` is a positive integer. The script includes test cases to demonstrate the function's behavior with valid and invalid input.