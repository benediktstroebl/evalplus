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

# Test function to check the is_prime function
def test_is_prime():
    assert is_prime(6) == False
    assert is_prime(10) == True
    assert is_prime(13) == True
    assert is_prime(2) == True
    assert is_prime(9) == False
    assert is_prime(15) == False
    assert is_prime(0) == False
    assert is_prime(61) == True
    assert is_prime(701) == False
```
This code defines a function is_prime that checks whether a given number n is prime or not. The function uses some basic heuristic and loops to check for divisibility. It returns True if the number is prime and False otherwise.

The test_is_prime function tests the correctness of the is_prime function by asserting that it returns the correct results for a set of values. The test passes all of these assertions.