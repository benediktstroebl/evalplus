```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in primes:
        if n % p == 0:
            return False

    c = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            c += 1
    return c == 3
```

The function `is_multiply_prime` checks if the given number is divisible by any prime number less than 100. If it is not, it proceeds to count the number of divisors of the given number, checking only up to the square root of the number. If the number has exactly 3 divisors, then it is indeed the multiplication of 3 prime numbers and the function returns `True`.

Here is a test that can be used to validate the function:
```python
assert is_multiply_prime(30)
assert not is_multiply_prime(28)
assert not is_multiply_prime(36)
assert is_multiply_prime(54)
```