```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function is crafted to evaluate whether a given number `n` is prime. It initiates by checking if `n` is less than 2, returning `False` if so, as numbers less than 2 are not prime. The function then commences a loop from 2 up to the square root of `n`, checking for divisibility. If `n` is divisible by any integer within this range, the function returns `False`, indicating that the number is not prime. However, if `n` surpasses the loop without finding a divisor, the function returns `True`, signifying that the number is prime. 

This structured approach enables the function to efficiently determine a number's primality based on a series of divisibility checks and a clear step-by-step process.