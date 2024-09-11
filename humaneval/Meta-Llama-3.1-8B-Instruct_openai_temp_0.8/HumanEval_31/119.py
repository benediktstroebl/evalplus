### Prime Number Check
#### Description
A Python script to check if a given number is prime or not.

#### Code

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Examples:
        >>> is_prime(6)
        False
        >>> is_prime(101)
        True
        >>> is_prime(11)
        True
        >>> is_prime(13441)
        True
        >>> is_prime(61)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
if __name__ == "__main__":
    print(is_prime(6))   # False
    print(is_prime(101)) # True
    print(is_prime(11))  # True
    print(is_prime(13441))  # True
    print(is_prime(61))   # True
    print(is_prime(4))    # False
    print(is_prime(1))    # False
```

#### Explanation
The `is_prime` function checks if a number `n` is prime by the following conditions:

- If `n` is less than 2, it is not prime.
- It then checks for divisibility from 2 to the square root of `n` (inclusive). If `n` is found to be divisible by any of these numbers, it is not prime.
- If `n` is not divisible by any of the numbers in the above range, it is prime.

The script includes example usage in the `if __name__ == "__main__":` block to verify that the function works as expected.