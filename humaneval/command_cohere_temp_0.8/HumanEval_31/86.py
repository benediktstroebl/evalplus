Here's a Python script with a self-contained function that solves the prime-checking problem, as described in the code block and tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This `is_prime` function iterates through numbers from 2 up to the square root of the input number `n`, checking for divisibility. If the number is divisible by any integer in that range, it's not prime, and the function returns `False`. If not, it returns `True`, indicating that the number is prime. This approach helps to efficiently rule out non-prime candidates and accurately determine primality. Feel free to test this function with more input numbers to verify its behavior.  This approach provides a succinct and efficient way to determine prime numbers.