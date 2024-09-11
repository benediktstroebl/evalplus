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

# Test cases
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, please note that this recursive implementation is not efficient for large values of `n` due to the repeated computation of the same subproblems. For larger values of `n`, it is better to use an iterative approach or a memoized function to store the results of expensive function calls.

Here is a more efficient version of the function using recursion and memoization:
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

# Test cases
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

Alternatively, you can use an iterative approach to calculate the Fibonacci number:
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
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Test cases
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```