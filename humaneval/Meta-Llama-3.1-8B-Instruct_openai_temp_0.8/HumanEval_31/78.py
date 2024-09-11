### Prime Number Checker
#### Python Script
```markdown
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # Numbers divisible by 2 or 3 are not prime
        return False
    i = 5
    while i * i <= n:  # Only need to check up to sqrt(n)
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Check every 6 numbers (i and i+2 are both factors of most numbers)
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
### Notes

This script uses a simple trial division method to check if a number is prime. The idea is to check divisibility only up to the square root of the number, and then increment by 6 each time (since every prime number is of the form 6k ± 1, where k is a positive integer).

This method is more efficient than checking all numbers up to the number itself, especially for larger inputs. However, for very large inputs, more advanced primality testing algorithms may be necessary.
```