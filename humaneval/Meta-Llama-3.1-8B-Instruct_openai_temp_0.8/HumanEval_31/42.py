```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # Check if the number is less than or equal to 1, in which case it is not prime.
    if n <= 1:
        return False
    # Check if the number is 2, which is the only even prime number.
    if n == 2:
        return True
    # Check if the number is even, in which case it is not prime.
    if n % 2 == 0:
        return False
    # Check odd factors up to the square root of the number.
    max_factor = int(n**0.5) + 1
    for i in range(3, max_factor, 2):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))# True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime` that checks if a given number is prime, and a series of test cases at the end to demonstrate its correctness. The function works by checking if the number is less than or equal to 1 (in which case it is not prime), if it is 2 (the only even prime number), if it is even (in which case it is not prime), or if it has any odd factors up to its square root (in which case it is not prime). If none of these conditions are met, the number is prime.