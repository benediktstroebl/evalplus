```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the range of numbers to sum.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    # Using the formula for the sum of an arithmetic series to optimize the calculation
    return n * (n + 1) // 2


# Example usage:
if __name__ == "__main__":
    print(sum_to_n(30))  # Outputs: 465
    print(sum_to_n(100))  # Outputs: 5050
    print(sum_to_n(5))  # Outputs: 15
    print(sum_to_n(10))  # Outputs: 55
    print(sum_to_n(1))  # Outputs: 1
```

This Python script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the mathematical formula for the sum of an arithmetic series, which is `n * (n + 1) / 2`, to optimize the calculation. This approach avoids the need to loop over the numbers from 1 to `n` and is therefore more efficient for large values of `n`. The script also includes example usage of the `sum_to_n` function.