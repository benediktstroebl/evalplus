```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n using the arithmetic series formula:
    sum = (n * (a1 + an)) / 2, where a1 is the first term and an is the last term.

    Args:
        n (int): The number up to which the sum is calculated.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")

    return (n * (n + 1)) // 2

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines the `sum_to_n` function that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the arithmetic series formula to calculate the sum efficiently. The function includes input validation to ensure that the input is a positive integer. Finally, the script includes test cases to demonstrate the function's correctness.