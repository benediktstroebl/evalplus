```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if the number is a multiplication of three primes. First, it generates a list of prime numbers up to the square root of the given number. Then, it finds all factors of the given number and checks if their amount is equal to 3 and that all of them are present in the list of primes. The markdown block contains the corresponding tests for the function. 

```python
# Tests for is_multiply_prime

def test_is_multiply_prime():
    assert is_multiply_prime(30)
    assert not is_multiply_prime(12)
    assert not is_multiply_prime(16)
    assert is_multiply_prime(54)
```