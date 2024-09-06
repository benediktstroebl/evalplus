```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function uses predefined list primes list of prime numbers below 100. Then it calculates the factors of the given integer n and checks whether their number is exactly 3 and they are a subset of the set of prime numbers. 

### Here is a test suite that can be used to validate the function:
```python
def test_is_multiply_prime():
    # True cases
    assert is_multiply_prime(30)
    assert is_multiply_prime(51)
    assert is_multiply_prime(74)
    # False cases
    assert not is_multiply_prime(6)
    assert not is_multiply_prime(8)
    assert not is_multiply_prime(10)
    assert not is_multiply_prime(98)
```