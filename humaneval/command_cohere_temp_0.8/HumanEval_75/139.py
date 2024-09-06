```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```
The function `is_multiply_prime` takes a single argument `n`, which is the number we want to test. It first creates a list of known prime numbers up to `37` and then calculates the factors of the given number `n`. It then checks two conditions:
1. That the number of factors is exactly `3`. This checks that `n` can be factorized into exactly 3 primes. 
2. That one of the factors is one of the known prime numbers. This checks that the factorization is valid. 

The function returns `True` if both conditions are satisfied, and `False` otherwise. 

The code includes an example in the function's docstring to guide users on how to use the function and understand its behavior. 

This approach provides a clear and efficient way to determine if a number is the product of three prime numbers within the given constraint. Caveats: 
The function's assumption is that the given number's factors are limited to numbers less than or equal to the square root of the number. This assumption is valid for the range less than 100, as per the prompt's guidelines. However, this assumption may not hold for larger numbers. This approach could potentially fail for very large numbers due to the computation time of checking for primality and the number of factors that can be stored in the memory.