### Prime Number Checker

Below is a Python function that checks if a given number is prime or not.

```markdown
### Code

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to be checked.

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
        # Numbers less than or equal to 1 are not prime
        return False
    elif n <= 3:
        # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:
        # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:
        # Check divisibility up to the square root of the number
        if n % i == 0 or n % (i + 2) == 0:
            # If the number is divisible, it's not prime
            return False
        i += 6
    # If no divisors are found, the number is prime
    return True
```

### Usage

You can use this function to check if a number is prime by calling it with the desired number as an argument.

```python
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

### Explanation

This function uses a simple trial division method to check for primality. It first checks for numbers less than or equal to 1, which are not prime. Then, it checks for numbers that are divisible by 2 or 3. Finally, it checks for divisibility up to the square root of the number. If no divisors are found, the number is considered prime. This approach is efficient because it only checks up to the square root of the number.