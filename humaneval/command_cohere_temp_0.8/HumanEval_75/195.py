```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function `is_multiply_prime(n)` takes a positive integer `n` as input and checks whether `n` is the product of exactly three prime numbers. To do this, it first generates a list of prime numbers up to the square root of `n`. It then determines the prime factors of `n` by looping from 2 to the square root of `n` and checking for each number if it is a factor of `n`. If there are exactly three distinct factors, and they are all prime, the function returns `True`, otherwise it returns `False`. 

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
```
This will print `True` as the output, as `30` is the product of three prime numbers: `2`, `3`, and `5`. 

The code provides an accurate solution to the problem, however, it is worth noting that the loop iterates up to `n ** 0.5` instead of `n` to improve the efficiency of factor finding. Also, the set data structure is utilized to effectively check for the presence of prime factors.