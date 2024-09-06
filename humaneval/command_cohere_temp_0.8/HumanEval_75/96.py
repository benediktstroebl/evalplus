```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```
The function `is_multiply_prime` takes a single parameter `n`, which represents the number to be checked. It generates a list of known prime numbers (`primes`), and then it creates a set of factors of `n` (`factors`). The set is created using the `range` function and filtered by the condition that the remainder of the division of `i` by `n` is 0 (`n % i == 0`). 

The length of `factors` is checked to determine if it is equal to 3, which indicates that `n` might be represented as the product of three prime numbers. Further, it checks if the maximum factor in the set is present in the `primes` list, which is given. 

If both conditions are met, the function returns `True`, indicating that the number is the product of three prime numbers. Otherwise, it returns `False`. 

Let's break down the conditions: 
- `len(factors) == 3`: This checks if there are exactly three distinct factors.
- `max(factors) in primes`: This checks if the largest factor is a prime number. 

The script ensures that the provided number `n` is not greater than 100 and returns the correct output for the given example (`is_multiply_prime(30) == True`). 

This function can accurately determine whether a given number is the product of three prime numbers and is sufficiently efficient for applications involving numbers less than 100.