### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```
### Usage Example
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (17 is a prime number)
print(largest_divisor(24))  # Output: 12 (24 = 3 * 2 * 2 * 2)
```
This script uses a simple iterative approach to find the largest divisor. It starts from `n - 1` and checks each number to see if it divides `n` evenly. As soon as it finds a divisor, it returns that number. If `n` is a prime number, the largest divisor will be 1.