```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime(n)` determines whether a given number `n` is prime. It begins by checking if `n` is less than 2, returning `False` if so, as prime numbers always exceed 1. The function then iterates through numbers from 2 up to the square root of `n`, checking whether `n` is divisible by any of them. If divisibility is found, the function returns `False`, indicating that the number is not prime. However, if no divisors are found, the function returns `True`, signifying that the number is prime. This method is efficient due to its use of the square root test, eliminating the need for checking larger multiples for divisibility.