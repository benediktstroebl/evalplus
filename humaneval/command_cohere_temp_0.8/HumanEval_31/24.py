```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality. It initiates by checking if the given number is less than 2, returning False if so, since primality is undefined for negative numbers or zero. The function then iterates through numbers from 2 up to the square root of the given number, checking for divisibility. If the number is divisible by any integer within this range, it's not prime, and the function returns False. However, if no divisors are found, the function returns True, indicating that the number is prime. This approach ensures that non-prime numbers, especially perfect squares, are accurately identified.