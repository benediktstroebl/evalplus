### Fibonacci Number Calculation

The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it. Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so forth.

Below is a Python function to calculate the nth Fibonacci number:

```python
def memo_fib(n: int, memo: dict = {}):
    """Return n-th Fibonacci number using memoization.
    >>> memo_fib(10)
    55
    >>> memo_fib(1)
    1
    >>> memo_fib(8)
    21
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = memo_fib(n-1, memo) + memo_fib(n-2, memo)
    return memo[n]


def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    return memo_fib(n)


# Test the function
for num in range(1, 11):
    print(f"Fibonacci number at position {num} is: {fib(num)}")
```

In this script, we define a `memo_fib` function that uses memoization to store previously calculated Fibonacci numbers. This approach prevents redundant calculations and reduces the time complexity of the function from exponential to linear. The `fib` function is a wrapper around `memo_fib` and provides the same functionality.

We then test the `fib` function by calculating the first 10 Fibonacci numbers and printing the results.