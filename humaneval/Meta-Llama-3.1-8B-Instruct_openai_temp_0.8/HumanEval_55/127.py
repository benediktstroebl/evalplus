### Fibonacci Number Calculator

This Python script calculates the nth Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is
    the addition of the last two numbers, starting with 0 and 1.

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
        return fib(n - 1) + fib(n - 2)


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i} is: {fib(i)}")
```

This script uses a recursive approach to calculate the nth Fibonacci number. However, please note that this approach is not efficient for large values of n due to the repeated computation of the same sub-problems. A more efficient solution would use dynamic programming to store the results of sub-problems and avoid redundant computation.

### Memoized Fibonacci Function (more efficient)

```python
def fib_memo(n: int) -> int:
    """
    Return n-th Fibonacci number using memoization.

    >>> fib_memo(10)
    55
    >>> fib_memo(1)
    1
    >>> fib_memo(8)
    21
    """
    memo = {0: 0, 1: 1}
    return fib_helper(n, memo)


def fib_helper(k: int, memo: dict) -> int:
    if k not in memo:
        memo[k] = fib_helper(k - 1, memo) + fib_helper(k - 2, memo)
    return memo[k]


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i} is: {fib_memo(i)}")
```

In this version, we use a dictionary `memo` to store the results of sub-problems. The `fib_helper` function uses this dictionary to avoid redundant computation and improves the efficiency of the Fibonacci calculation.