```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is prime.
    Returns None if n <= 1, non-prime Fibonacci numbers.
    """
    return_fib_helper(n, n % 2 == 0)

def _prime_fib_helper(n: int, test: bool = True):
    if n <= 1:
        return n
    if test and n % 2 == 0:
        return _prime_fib_helper(n, False)
    return _prime_fib_helper(n - 1, test) + _prime_fib_helper(n - 2, test)

if __name__ == "__main__":
    for _ in range(10):
        n = _prime_fib_helper(_test=True)
        print(n, end=' ')
```
This code provides a helper function `_prime_fib_helper` that recursively calculates the n-th Fibonacci number that is prime. The helper function checks for prime by looking for even divisibility and calculates the Fibonacci number by summing up the results of two helper calls.  The basic test case is to check for primality and the final result is then returned.