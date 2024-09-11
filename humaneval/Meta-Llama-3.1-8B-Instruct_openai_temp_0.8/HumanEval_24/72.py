### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): A positive integer.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from the largest possible divisor (n // 2) and decrement until we find a divisor
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Example usage
if __name__ == "__main__":
    print(largest_divisor(15))  # Output: 5
    print(largest_divisor(20))  # Output: 10
    print(largest_divisor(30))  # Output: 15
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It uses a simple loop to iterate from the largest possible divisor (half of `n`) down to 1 and checks if each number is a divisor of `n`. The first divisor found is returned as the result. The script also includes example usage to demonstrate how to call the function.