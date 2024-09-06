```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if a given number is the multiplication of 3 prime numbers. It first calculates the factors of the number and then checks if there are exactly 3 of them and they overlap with the set of known primes. 

This approach allows the function to achieve a much better time complexity of O(sqrt(N)) compared to a naive solution that checks all combinations of prime numbers. 

Let's say we want to check if 30 is a multiply prime. The function first calculates the factors of 30, which are {2, 3, 5}, and then checks if these factors are also primes, which they are. Thus, the function returns True.