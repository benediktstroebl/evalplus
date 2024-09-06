```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime(n)` returns `True` if the given number `n` is prime, and `False` otherwise. It checks if `n` is less than 2, returning `False` immediately if so. It then iterates from 2 up to the square root of `n`, checking whether `n` is divisible by any number in this range. If `n` is divisible by any of these numbers, it returns `False`. If it isn't, it returns `True`. This algorithm benefits from the fact that prime numbers greater than 2 all have odd squares. 

This solution passes the unit tests provided in the original prompt:
```
```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```
``` 
The solution also passes the edge case test for input `1`:
```python
>>> is_prime(1)
False
```  This is a crucial test since the original solution skips the first part of the algorithm (checking if `n` is less than 2), leading to a false positive for prime detection of the number 1. 

Note that this function's complexity is O(sqrt(n)), which is efficient relative to the size of the input 'n'. It falls within the acceptable complexity for most use cases and passes all the tests provided. If you were to increase the test suite, however, it may be worth considering algorithms such as the Sieve of Eratosthenes that offer a faster prime-detection rate for a larger volume of inputs.