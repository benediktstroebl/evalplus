```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        # Check if n-1 is a prime
        is_prime = True if n - 1 >= 2 else False
        if is_prime:
            # Calculate the n-th Fibonacci number and check if prime
            return _prime_fib(n, 2)
        else:
            return _prime_fib(n, 3)

def _prime_fib(n: int, inc: int) -> int:
    if n <= inc:
        return 0
    result = 1
    for _ in range(1, n - inc + 1):
        result *= inc
        result += _prime_fib(n, inc + 1)
    return result
```
This function solves the n-th Fibonacci number and returns it as a prime.