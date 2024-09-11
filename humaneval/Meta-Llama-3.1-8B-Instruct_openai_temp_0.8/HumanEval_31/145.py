### Prime Number Checker
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    
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
    
    # If no factors found, n is prime
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
This script uses a simple and efficient algorithm to check if a given number is prime. It handles corner cases (numbers less than 2) and uses a loop to check odd factors up to the square root of the number. If no factors are found, the number is considered prime. The test cases at the end demonstrate the function's behavior with various inputs.