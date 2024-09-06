```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 2  # base case
        # check for each number after base case
        for i in range(3, n + 1):
            if is_prime(i):
                return i
        return n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True
```

This function uses a simple algorithm to check if a given number is prime or not. It iterates through numbers from 2 up to the square root of the number, then checks if the number is divisible by any of those numbers.  It returns `True` if the number is not divisible by any of those, indicating it's prime.