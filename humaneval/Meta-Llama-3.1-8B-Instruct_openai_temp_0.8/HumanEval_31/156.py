### Prime Number Checker
A Python function to determine whether a given number is prime or not.

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # We only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # Only check odd divisors
        if n % d == 0:
            return False
    return True

# Example usage:
if __name__ == "__main__":
    print(is_prime(6))    # False
    print(is_prime(101))  # True
    print(is_prime(11))   # True
    print(is_prime(13441))# True
    print(is_prime(61))   # True
    print(is_prime(4))    # False
    print(is_prime(1))    # False
```

This function works by first checking for the base cases where `n` is less than or equal to 1, or where `n` is 2 (the only even prime number). It then checks if `n` is even, in which case it immediately returns `False` since all other even numbers are not prime.

Next, the function calculates the square root of `n` and adds 1 to it. It then uses a loop to check for odd divisors of `n` up to the calculated maximum divisor. If any divisor is found, the function returns `False`. If the loop completes without finding a divisor, the function returns `True`, indicating that `n` is prime.