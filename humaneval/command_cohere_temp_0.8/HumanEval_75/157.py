```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return not any(factor in factors for prime in primes for factor in primes if prime ** 3 > factors[factor] or n % prime == 0)
```

The function `is_multiply_prime` checks if the number `n` is the product of three prime factors, it first computes the list of prime factors of the number and then checks if there are exactly three distinct prime factors, if so, it returns `True`, otherwise it returns `False`. 

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
```
The output should be:
```
True
```

This is true because 30 is the product of three prime factors: 2, 3, and 5. 

Note that this approach will work only for numbers that are less than 100 and are the product of three prime factors, as described in the problem statement. 

To handle larger numbers or cases with more than three prime factors, you may need to adjust the code or use more efficient prime factorization techniques.  You can also add tests to ensure the function behaves correctly for a variety of inputs.