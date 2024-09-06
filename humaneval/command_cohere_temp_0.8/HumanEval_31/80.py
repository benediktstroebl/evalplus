```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function iterates through numbers from 2 up to the square root of the input number `n`, checking whether `n` is divisible by any of these numbers. If it's not divisible by any, it's considered prime. This aligns with the mathematical definition of a prime number, ensuring that the code provides accurate results for prime checking.