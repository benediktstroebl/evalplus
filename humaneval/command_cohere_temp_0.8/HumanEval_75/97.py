```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```

The function `is_multiply_prime` checks if a given number is the multiplication of three prime numbers. It first calculates the factors of the input number and then checks if there are exactly three of them and that the largest one is amongst the known prime numbers.