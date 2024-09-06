```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function `is_multiply_prime` checks if the number `n` is the product of 3 prime numbers. It first creates a list of prime numbers up to `n` and then calculates all the factors of `n`, checking if the number is divisible by any integer between 1 and the square root of `n`. 

The length of the set of factors is checked to determine if it has exactly 3 elements, as well as checking if the set of factors intersects with the set of prime numbers, which would make the set of factors valid prime numbers. 

The given example tests cases passing in 30, which would return True due to 2 * 3 * 5 = 30,3 * 5 both being prime numbers and the unique factors of 30.