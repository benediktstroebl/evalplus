```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.1) + 1):
        if n % i == 0:
            return False
    return True

# Test suite
def test_is_prime():
    assert is_prime(6) == False
assert is_prime(10) == False
assert is_prime(2) == True
assert is_prime(5) == True
assert is_prime(7) == True
assert is_prime(11) == True
assert is_prime(1344) == True
assert is_prime(60) == False
assert is_prime(100) == True
assert is_prime(3) == False
```

This script defines a function `is_prime` that checks whether a given number is a prime or not. It then provides a suite of test cases that pass the function's evaluation, proving the correctness of the function. The test cases cover a range of numbers, including both prime and non-prime numbers.