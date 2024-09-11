### Fibonacci Number Calculation
#### Simple Recursive Implementation

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.

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
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i} is: {fib(i)}")
```

However, the recursive solution has an exponential time complexity due to repeated computations. For large values of `n`, it's more efficient to use an iterative approach or memoization to store and reuse previously calculated Fibonacci numbers.

#### Memoized Recursive Implementation

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.

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
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i} is: {fib(i)}")
```

#### Iterative Implementation

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.

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

# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i} is: {fib(i)}")
```

Choose the implementation that best suits your needs based on time complexity and code complexity considerations.