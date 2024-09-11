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
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i += 6
    return True


# Test the function
if __name__ == "__main__":
    print(is_prime(6))  # Output: False
    print(is_prime(101))  # Output: True
    print(is_prime(11))  # Output: True
    print(is_prime(13441))  # Output: True
    print(is_prime(61))  # Output: True
    print(is_prime(4))  # Output: False
    print(is_prime(1))  # Output: False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a simple trial division method to check for primality. The function first checks for numbers less than or equal to 1, which are not prime. Then it checks for numbers less than or equal to 3, which are prime. Next, it checks if the number is divisible by 2 or 3, in which case it's not prime. Finally, it uses a while loop to check if the number is divisible by any other number up to its square root.