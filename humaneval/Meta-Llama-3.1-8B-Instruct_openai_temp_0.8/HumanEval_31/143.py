```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    elif n <= 3:  # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:  # If n is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # Only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisibility by 6k ± 1
            return False
        i += 6
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script uses a helper function to check if a number is prime. It first checks for the base cases where the number is less than or equal to 1, or is 2 or 3 (which are prime). Then it checks if the number is divisible by 2 or 3. If neither of these conditions are met, it checks for divisibility by 6k ± 1 (which are the possible factors of odd numbers greater than 3). If none of these conditions are met, the number is prime.