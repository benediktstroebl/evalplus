```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    else:
        return 3
    
    # Check for primality using trial division method
    for i in range(4, n + 1, 2):
        if is_prime(i):
            return i
    return None

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

# Test the prime_fib function
print(prime_fib(5))
```

The code defines a function `prime_fib` that computes the n-th Fibonacci number that is prime and returns it. The function first checks if n is less than or equal to 1 and returns n directly. Then, it checks if n is even a power of 2 and returns 2 if it's so. If n is not a power of 2, it uses the trial division method to find the next prime number. The function then loops from 4 to the square root of n, testing each number to see if it is prime or not. Finally, the function returns `None` to indicate that the function has completed without finding a prime Fibonacci number for that input.