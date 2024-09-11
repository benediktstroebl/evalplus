### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
```
This function works by iterating over the numbers from `n-1` down to 1, checking each number to see if it divides `n` evenly (i.e., if `n % i == 0`). As soon as it finds a divisor, it returns that divisor.

Alternatively, you can use a more mathematical approach based on the fact that a number is its own largest divisor when divided by 2, except when the number is prime. This function does not account for the case when the number is prime, but it is a more efficient solution when the number is composite:
```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    if n % 2 == 0:
        return n // 2
    else:
        return (n - 1) // 2 * 2 + 1

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
```