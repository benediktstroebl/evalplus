Here's a Python script with a self-contained function `is_prime` that follows the problem statement and hopefully passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function iterates through numbers from 2 up to the square root of the input number `n`, checking for divisibility. If the number is divisible by any integer within this range, it's not prime, and the function returns `False`. If no divisors are found, it's a prime number, and the function returns `True`. 

This approach allows for a linear time complexity, optimizing the prime-checking process for larger numbers. It's a common optimization since prime numbers larger than 2 always include at least one factor between 2 and its square root.