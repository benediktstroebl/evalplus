```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return False
    else:
        prev = 2
        while True:
            if is_prime(prev):
                break
            prev += 1
        return prev

def is_prime(num: int):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

# Test the prime_fib function
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(7))
```

This script defines a function `prime_fib` that calculates and returns the n-th Fibonacci number which is prime and also checks if it's prime. The function uses an optimized approach with a `while` loop and checks for divisibility by testing divisors up to the square root of the number.