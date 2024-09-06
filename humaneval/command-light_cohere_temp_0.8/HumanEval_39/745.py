Here's a Python script with a self-contained function that solves the problem of finding the n-th Fibonacci number that is also prime:
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
        return None
    fib = [0, 1]
    for _ in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    for _ in range(2, n // 2 + 1):
        if is_prime(fib[-1]):
            fib.append(fib[-1] + fib[-2])
    return fib[-1]
```
This script defines two functions: `is_prime` checks whether a given number is prime, and `prime_fib` computes the n-th Fibonacci number that is prime. The function then generates a list of Fibonacci numbers, iteratively calculates the Fibonacci number by summing up the two preceding numbers. It then uses the general prime test logic to check if each Fibonacci number is prime. The function then returns the Fibonacci number that is the largest prime number less than or equal to n.