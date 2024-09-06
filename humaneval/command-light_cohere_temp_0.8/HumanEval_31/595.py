```python
def is_prime(n):
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

# Test function
def test_is_prime():
    assert is_prime(6) == True
    assert is_prime(10) == False
    assert is_prime(2) == True
    assert is_prime(5) == True
    assert is_prime(7) == False
    assert is_prime(14) == False
    assert is_prime(49) == True
    assert is_prime(101) == True
    assert is_prime(13441) == True
    assert is_prime(61) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
```

This script provides a function that checks whether a given number is a prime or not. The function uses a loop and several small numbers as tests to determine whether the number is prime or not.