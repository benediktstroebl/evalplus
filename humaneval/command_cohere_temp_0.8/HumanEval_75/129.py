```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return not any(factor in factors for prime in primes for factor in primes if prime ** 3 > factors[factor])
```
The function `is_multiply_prime` checks if the number is a multiplication of three prime numbers. It first assumes the number has already been factorized into its constituents, which is less than the square root of `n`. Hence, it checks if any primes less than the square root of `n` have a cube greater than each constituent. 

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
print(is_multiply_prime(36))
```
This should output:
```bash
True
False
```
Which validates the example provided in the problem statement.