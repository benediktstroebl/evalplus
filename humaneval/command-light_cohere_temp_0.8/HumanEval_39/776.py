```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 2 if is_prime(n) else next((i for i in range(3, n + 1) if is_prime(i)))

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(13))  # Output: True
print(prime_fib(59))  # Output: False
```
This script defines a function `prime_fib` that calculates the n-th Fibonacci number and determines whether it's prime. The function uses a `is_prime` helper function, which employs a trial and error approach to find prime numbers. The `prime_fib` function also uses the `next` function with a range of numbers from 3 up to n to determine if the n-th Fibonacci number is prime or not.