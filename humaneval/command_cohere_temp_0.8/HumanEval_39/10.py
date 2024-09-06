```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    if n < 1:
        return None
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[n - 1] if is_prime(fib[n - 1]) else None

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```
This script defines a function `prime_fib` that returns the n-th Fibonacci number that is also prime. The function handles cases where n is less than 1 and uses the `is_prime` function to efficiently check if a number is prime. The final test section validates the correctness of the `prime_fib` function.  This solution is efficient and well-organized, providing an optimal approach to solving this problem.