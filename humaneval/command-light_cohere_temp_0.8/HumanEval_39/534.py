Here is a self-contained Python function that solves the Fibonacci prime problem:
```python
def is_prime(n):
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

def prime_fib(n):
    if n <= 0:
        return
    if n == 1:
        return 2
    if n == 2:
        return 3
    fib = 2
    while fib < n:
        if is_prime(fib):
            yield fib
            fib += 1
        else:
            fib += 2
    yield n

# Test the function
for i in range(1, 10):
    print(f"{i} is prime:", end="\n")
    print(str(is_prime(i)))

# Test the function with some large values
print(f"{10}", end="is prime:", end="\n")
print(str(is_prime(10)))
```

This script defines two functions: `is_prime` checks if a given number is prime, and `prime_fib` generates and yields the n-th Fibonacci prime number. The `for` loop at the generates and prints all prime numbers up to 10, and also tests the function with some larger values.