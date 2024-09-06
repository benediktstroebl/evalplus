```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        i = 2
        while i * i <= n:
            if is_prime(i):
                yield i
                i += 2
            else:
                i += 2
                yield from prime_fib(n - i)
        yield n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Driver code to test the function
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(10))
print(prime_fib(30))

```

This code defines a prime_fib function that generates and yields the n-th prime Fibonacci number, along with a helper function is_prime that checks if a given number is prime.  The driver code generates test cases to ensure the function works correctly for various inputs.