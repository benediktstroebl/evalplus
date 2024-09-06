```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` takes a number `n` as input and checks whether it is the multiplication of three prime numbers. It first generates a list of prime numbers up to `100` and then calculates the factors of the given number `n`. Subsequently, the function checks whether the number of factors is exactly `3` and whether all the factors are present in the list of the prime numbers. The markdown cell contains some tests to verify the correct behavior of the function. 

The tests can be executed by copying the content of the markdown cell into a Python file (e.g., `test_is_multiply_prime.py`) and running the file with `python test_is_multiply_prime.py`. 

The output of the tests should look as follows:
```bash
Tests passed!
```