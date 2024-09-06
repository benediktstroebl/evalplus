```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and sorted(factors) in primes
```
The function `is_multiply_prime` checks if the number is the multiplication of three primes. First, it generates a list of primes from 2 to `n`, then it calculates the factors of the number, and finally, it checks if the number of factors is exactly 3 and that the factors are in the prime list. 

Here is a test to check the above function:
```python
assert is_multiply_prime(30)
assert not is_multiply_prime(52)
```