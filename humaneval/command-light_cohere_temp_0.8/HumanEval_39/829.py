```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        return prime_fib(n // 2) + next((6,), seeds=[2, 3])[0]

# Test
def test_prime_fib(test_case: int):
    assert prime_fib(test_case) == test_case

# Test cases
test_prime_fib(5)
test_prime_fib(6)
test_prime_fib(8)
test_prime_fib(10)
```
The code defines a function `prime_fib` that calculates the n-th Fibonacci number that is also prime, where n is greater than 1. It uses a strategy to determine primality by testing divisibility with 2 and selecting the next seed from an array of pairs (6 included). The test suite consists of test cases, which use the `test_prime_fib` function to check the correctness of the `prime_fib` function.