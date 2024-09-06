```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime` takes a single argument `n`, which represents the number whose primality is to be checked, and returns `True` if the number is prime and `False` otherwise. It operates by iteratively checking whether the number can be divisible by any number from 2 to the square root of the number, if it isn't, then it is prime. 

However, it's worth mentioning that this function isn't suited for checking the primality of very large numbers due to the excessive time taken to execute. Instead, the primality of large numbers can be checked using more efficient algorithms like the Miller-Rabin primality test.