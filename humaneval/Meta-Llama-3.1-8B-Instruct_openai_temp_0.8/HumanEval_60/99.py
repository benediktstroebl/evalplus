### Summation Function
```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the summation.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Using the formula for the sum of an arithmetic series: n*(n+1)/2
    return n * (n + 1) // 2

# Example use cases
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the formula for the sum of an arithmetic series, which is `n*(n+1)/2`, to calculate the sum. The script also includes example use cases to demonstrate the function's behavior. Note that the function raises a `ValueError` if `n` is not a positive integer.