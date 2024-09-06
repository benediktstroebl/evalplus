```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [val for val in primes if n % val == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime(n)` uses a list of known prime numbers (`primes`) to determine if the given number (`n`) is divisible by each of these primes. If the number has exactly three distinct divisors, then it is considered to be the product of three prime numbers, and the function returns `True`. Otherwise, it returns `False`.

Here's a test to see if the function works as intended:
```python
def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(52) == False
    assert is_multiply_prime(100) == False
```

The example provided in the problem statement is also tested to ensure the function behaves as expected.

This should allow you to accurately determine if a number is the product of three prime numbers.