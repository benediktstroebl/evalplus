```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function incorporates an optimization strategy employed to sieve out prime numbers, which is a critical time-saving technique. The routine checks if the number `n` is less than 2; if so, it returns `False`, denoting that the number is not prime. The function subsequently cycles through numbers from 2 up to the square root of `n` (inclusive), meticulously assessing whether `n` is divisible by any of these numbers. If such a divisor is found, the function returns `False`, indicating that the number is not prime. If no divisors are encountered in the loop, the function returns `True`, indicating that `n` is indeed a prime number. This method is both accurate and efficient, enabling the identification of prime numbers with minimal computational complexity.