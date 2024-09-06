```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach accented by a wrinkle: the limit for square root iterations is `int(n ** 0.5) + 1`. This improvement eliminates the need for checking divisors beyond the square root, optimizing performance for a crucial scenario.

The function suits the provided tests, including:
```python
> is_prime(6)
False
> is_prime(101)
True
> is_prime(11)
True
> is_prime(13441)
True
> is_prime(61)
True
> is_prime(4)
False
> is_prime(1)
False
```

This refined function balances simplicity and efficiency to reliably solve the problem.