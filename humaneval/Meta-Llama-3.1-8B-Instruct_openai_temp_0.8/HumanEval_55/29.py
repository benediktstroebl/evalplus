### Fibonacci Number Generator
#### Recursive Implementation
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
Note: This recursive implementation is not efficient for large `n` due to repeated calculations. For a more efficient solution, consider using memoization or dynamic programming techniques.

#### Memoized Implementation
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    memo = {0: 0, 1: 1}

    def fib_helper(k: int) -> int:
        if k not in memo:
            memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]

    return fib_helper(n)


# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This memoized implementation stores previously computed Fibonacci numbers in a dictionary to avoid redundant calculations.