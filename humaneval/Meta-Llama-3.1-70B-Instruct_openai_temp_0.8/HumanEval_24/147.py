```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for

    Returns:
        int: The largest number that divides n evenly, smaller than n
    """
    # Check if n is less than or equal to 1, in which case the function is undefined
    if n <= 1:
        raise ValueError("Input must be greater than 1")

    # Start from n - 1 and go downwards to find the largest divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i


# Example usage
if __name__ == "__main__":
    assert largest_divisor(15) == 5
    assert largest_divisor(17) == 1
    assert largest_divisor(100) == 50
```
This script defines a function `largest_divisor` that takes an integer `n` and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates over numbers from `n-1` downwards and checks if each number is a divisor of `n` by using the modulo operator (`%`). The first number that is a divisor is returned as the result. If `n` is less than or equal to 1, the function raises a `ValueError`. The script includes example usage and assertions to demonstrate the function's correctness.