```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function rigorously checks whether a given number `n` is prime. It begins by ruling out the special case of `n < 2`, which ensures timeliness. The function then iterates through numbers from 2 up to the square root of `n`, checking for divisibility. If the number is divisible by any iteration, it's not prime, and the function returns `False`. If no divisor is found after the loop, the number is prime, and the function returns `True`. 

This approach is efficient due to its use of the square root rule, which minimizes the number of iterations required to determine primality effectively. It's a robust solution for detecting prime numbers.