```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime(n)` determines if a given number is prime or not. It begins by checking if the given number is less than 2, returning False immediately if so. The function then iterates through numbers from 2 to the square root of the given number, checking whether the given number is divisible by any of them. If the number is divisible by any, it returns False, indicating that the number is not prime. However, if the loop completes without finding a divisor, it returns True, indicating that the number is prime. This approach efficiently determines primality with a simple implementation.