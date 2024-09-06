```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

# Test suite
def test():
    print(is_prime(6))     # Should return True
print(is_prime(101))  # Should return True
print(is_prime(11))  # Should return True
print(is_prime(13441))# Should return True
print(is_prime(61))   # Should return True
print(is_prime(4)))    # Should return False
print(is_prime(1))   # Should return False
``` 

This code defines a function that checks whether a given number is a prime. It then provides a suite of tests to check the correctness of the `is_prime` function.  The main goal of this code is to evaluate and test the primality-checking functionality.