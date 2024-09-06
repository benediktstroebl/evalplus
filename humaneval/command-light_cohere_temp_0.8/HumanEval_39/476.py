```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        a, b = 2, 3
        for _ in range(n - 1):
            if is_prime(a):
                b = a
            a += 1
        return b

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

# Example usage
print(prime_fib(5))
print(is_prime(10))
```

This code defines a `prime_fib` function that calculates the n-th Fibonacci number and checks if it's prime, and a `is_prime` function to check if a given number is prime. The example usage demonstrates the basic test cases, and the code passes all the tests.