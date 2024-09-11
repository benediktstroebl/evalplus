### Prime Number Checker
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:
        # 2 is the only even prime number
        return True
    if n % 2 == 0:
        # All other even numbers are not prime
        return False
    # Check odd factors up to the square root of n
    max_factor = int(n ** 0.5) + 1
    for i in range(3, max_factor, 2):
        if n % i == 0:
            # If n is divisible by any odd number, it's not prime
            return False
    # If no factors are found, n is prime
    return True

# Test cases
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```
This script defines the `is_prime` function, which checks whether a given number `n` is prime or not. It first handles the edge cases (numbers less than or equal to 1, and the number 2), and then checks for factors of `n` up to its square root. If any factors are found, `n` is not prime; otherwise, it is prime. The test cases at the end verify the correctness of the function.