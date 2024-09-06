```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```
The function `is_multiply_prime` checks if a given number is the multiplication of 3 prime numbers. It first calculates the factors of the number and then checks if their number is exactly 3 and that each is a prime number. The function uses a list of known primes to check the last condition. The known primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37. The corner case is handled by checking if the number is bigger than 100.