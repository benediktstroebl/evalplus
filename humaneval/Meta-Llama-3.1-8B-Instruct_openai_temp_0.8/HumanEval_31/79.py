### Prime Number Checker
#### Python Implementation

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    :param n: The number to check for primality.
    :return: True if n is prime, False otherwise.
    """
    # Corner cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    # If no factors are found, n is prime
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It returns `True` if `n` is prime and `False` otherwise. The function uses a combination of corner cases, even number checks, and odd factor checks to efficiently determine primality. The example usage section demonstrates the function's behavior with various inputs.