```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime` takes a single argument `n`, which represents the number to be checked for primality. It first handles the special case of n being less than 2, returning `False` in such cases. It then iterates through numbers from 2 to the square root of `n`, checking for divisibility. If `n` is divisible by any of these numbers, it returns `False`, indicating that `n` is not prime. However, if `n` is not divisible by any of these numbers, it returns `True`, indicating that `n` is prime. 

The tests are self-explanatory and ensure that the function behaves as expected for various cases. 

This function is efficient due to its use of the square root technique, which reduces the number of iterations required to check for primality. 

I hope this helps! Let me know if you have any further questions or if you would like to discuss more details.