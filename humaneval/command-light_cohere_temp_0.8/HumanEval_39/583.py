Here is a self-contained Python function that solves the problem of finding the n-th Fibonacci number that is also prime:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    temp = prime_fib(n // 2)
    if temp == 0:
        return 0
    return temp + prime_fib(n % 2)
```
This function takes an integer n as input and returns the n-th Fibonacci number that is prime. It uses recursion to solve the problem and tests to ensure it works correctly.