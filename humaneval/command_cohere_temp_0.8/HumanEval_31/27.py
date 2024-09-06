```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a loop from 2 to `n**0.5` to check for divisibility. If a divisor is found, the number is not prime, and the function returns False. If no divisors are found, the number is prime, and the function returns True. This method efficiently detects prime numbers while avoiding the pitfalls of less rigorous methods.