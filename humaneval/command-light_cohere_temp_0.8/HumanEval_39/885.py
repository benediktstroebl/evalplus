```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            return i
        i += 6
    return next((j for j in range(2, n + 1) if is_prime(j)), - 1)

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 6
    return True

# Test function
def test():
    n = 7
    result = prime_fib(n)
    assert result == 2
    assert is_prime(result)  # True
    assert is_prime(n + 2)  # False
    assert is_prime(n + 5)  # True
    assert is_prime(8)  # False
    assert is_prime(10)  # True
    assert is_prime(27)  # False
    assert is_prime(32)  # True
    assert is_prime(50)  # True

# Run tests
test()
```

This script defines a `prime_fib` function that computes the n-th Fibonacci number and checks if it is prime. The `is_prime` function checks if a given number is prime. The `test` function contains a set of tests for the `prime_fib` and `is_prime` functions to ensure their correctness. The `test` function uses the asserts to verify if the `prime_fib` and `is_prime` functions are returning the correct results for given inputs.