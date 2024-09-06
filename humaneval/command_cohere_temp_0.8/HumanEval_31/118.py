```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime` takes an integer `n` as input and checks if it is prime or not. It first checks if `n` is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of `n` (inclusive), and for each number `i`, it checks if `n` is divisible by `i`, if so, it returns `False`. If no divisors are found, it returns `True`, indicating that the given number is prime. 

This approach, called the **Sieve of Eratosthenes**, is efficient and avoids looping through every element up to `n`.