```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, a + 1) if a % i == 0)
    return not any(factor in primes for factor in factors)
```

The function `is_multiply_prime(a)` determines whether the number `a` is the product of three prime numbers by first establishing a list of prime numbers up to `a` and then verifying whether any integer between one and `a` that divides `a` is present in the list of primes. The algorithm yields `True` if no such integer is found.

Here is a simple test suite to ensure the function behaves as expected:
```python
def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(52) == False
    assert is_multiply_prime(100) == False
```