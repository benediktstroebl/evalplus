```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Raises:
        ValueError: If n is less than or equal to 1.
    """
    if n <= 1:
        raise ValueError("Input should be greater than 1")

    # Start checking from n-1, because n itself will be the largest divisor for sure
    # But we need the largest divisor smaller than n
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Expected output: 5
```
However, the code above is not very efficient, especially when dealing with large numbers, because it checks all numbers from `n-1` down to `1`. Here's a more efficient solution:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Raises:
        ValueError: If n is less than or equal to 1.
    """
    if n <= 1:
        raise ValueError("Input should be greater than 1")

    # Start checking from n-1, because n itself will be the largest divisor for sure
    # But we need the largest divisor smaller than n
    for i in range(n - 1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

    # If no divisor found, then n is a prime number and its largest divisor smaller than n is 1
    return 1


# Test the function
print(largest_divisor(15))  # Expected output: 5
```
Alternatively, we can also use the fact that a larger factor of the number must be a multiple of smaller factor that has already been checked. Therefore, we only need to check up to the square root of `n` to find its largest divisor.

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Raises:
        ValueError: If n is less than or equal to 1.
    """
    if n <= 1:
        raise ValueError("Input should be greater than 1")

    # Start checking from 2, because 1 is a divisor for all numbers
    for i in range(2, math.isqrt(n) + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            return max(i, n // i)

    # If no divisor found, then n is a prime number and its largest divisor smaller than n is 1
    return 1


# Test the function
print(largest_divisor(15))  # Expected output: 5
```