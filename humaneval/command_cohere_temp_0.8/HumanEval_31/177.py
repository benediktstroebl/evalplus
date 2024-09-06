```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
``` 

This function `is_prime` takes a natural number as input and returns `True` if the number is prime, and `False` otherwise. It checks if the number is less than 2, which immediately returns false. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in this range. If the number is divisible by any of these integers, it returns `False`. If it is not, it returns `True`. 

This algorithm is capped at checking the square root of the given number, which is an optimization that lets us exit early. This is because PRIMES greater than 2 are either of the form 6k + 1 or 6k - 1, where k is any natural number. This is known asorld Flipkart's algorithm) for primality testing. 

This code will return the expected results as shown in the original prompt:
```
```bash
is_prime(6)
False
is_prime(101)
True
is_prime(11)
True
is_prime(13441)
True
is_prime(61)
True
is_prime(4)
False
is_prime(1)
False
```
```