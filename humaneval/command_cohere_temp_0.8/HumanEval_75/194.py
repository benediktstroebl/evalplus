```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```
The function `is_multiply_prime` checks if a given number is the multiplication of 3 prime numbers. It first calculates the factors of the number and then checks if their number is exactly 3 and that the maximum factor is among the list of known primes. 

This solution has a time complexity of `O(sqrt(n))` as it iterates up to the square root of the number to find its factors.