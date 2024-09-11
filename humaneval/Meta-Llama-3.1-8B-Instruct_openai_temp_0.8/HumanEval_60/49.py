### Sum of Numbers from 1 to n

Below is a self-contained Python script that calculates the sum of numbers from 1 to n.

```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    return n * (n + 1) // 2


# Test the function
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1
```

This script uses the formula for the sum of an arithmetic series: `n * (n + 1) / 2` to calculate the sum of numbers from 1 to n. This approach is more efficient than summing numbers iteratively, especially for large values of n. The result is then printed to the console.