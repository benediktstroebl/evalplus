```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function returns True if the number is prime, and False otherwise. It first checks if the number is less than 2, and returns False if so. Then, it iterates through each number from 2 to n, and returns False if the number is divisible by any of them. If it is not divisible by any of them, it returns True. The tests provided in the prompt return True for prime numbers and False for non-prime numbers. Thus, the function correctly determines primality.