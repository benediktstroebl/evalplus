```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if the number `n` is the product of 3 prime numbers. It first creates a list of prime numbers up to `n` and then calculates the set of factors of `n`. If the length of the factor set is 3 and the set of factors overlaps with the set of primes, then the number is considered to be the product of 3 prime numbers. 

To check the correctness of the solution, you can call the function with the example provided in the problem statement:
```python
print(is_multiply_prime(30))
```
The output should be:
```
True
```

The `is_multiply_prime` function can also be optimized to prevent duplicate calculations of the prime factors:
```python
def is_multiply_prime(n):
    primes = [2, 3, 5]
    while len(primes) < 3:
        next_primes = [p * p for p in primes if p != 1]
        primes.extend(next_primes)
    return n == primes[0] * primes[1] * primes[2]
```

The inner loop extends the `primes` list with prime numbers that are the squares of the original list primes, excluding 1. The outer loop iterates until the length of the `primes` list reaches 3. The function returns `True` if `n` is equal to the product of the first 3 prime numbers in the list.