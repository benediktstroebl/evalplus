```python
# sum_to_n.py

def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

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

# Example usage
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"The sum of numbers from 1 to {n} is: {sum_to_n(n)}")
```

This script uses the mathematical formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to `n`. The formula is `n * (n + 1) / 2`, which is then divided by 2 to get the accurate result.

In the example usage section, it iterates over the numbers 1 to 10 and prints the sum for each number.