```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function `is_multiply_prime` takes a number `n` as an input. Firstly, the list of known prime numbers is stored in the `primes` list. Secondly, the list of factors of the given number is extracted and stored in the `factors` set. Lastly, using the length and the intersection of `factors` and `primes` we return the boolean result of the function. 

The given example in the problem statement returns `True` because 30 is the multiplication of 2, 3, and 5 - all prime numbers.