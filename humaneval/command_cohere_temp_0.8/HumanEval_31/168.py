```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a loop from 2 to `n ** 0.5` to check for divisibility. If the number is divisible by any integer within this range, it returns `False`, indicating that the number is not prime. However, if the number is not divisible by any integer within this range, it returns `True`, indicating primality. This process ensures that the function can efficiently determine whether a number is prime without any improper exceptions or hacks.