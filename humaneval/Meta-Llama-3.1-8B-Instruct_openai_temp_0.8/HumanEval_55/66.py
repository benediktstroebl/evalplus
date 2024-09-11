### Fibonacci Number Generator
#### Problem Statement
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. In this problem, we are asked to generate the n-th Fibonacci number.

#### Solution
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.

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

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, the above recursive solution is not efficient for large values of `n` due to the repeated computation of the same Fibonacci numbers. We can improve the efficiency by using a technique called "memoization", which stores the results of expensive function calls and returns the cached result when the same inputs occur again.

Here's the improved version:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.

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

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This version uses a dictionary `memo` to store the Fibonacci numbers as they are generated. If the Fibonacci number for a given `k` is already in the dictionary, it returns the cached result; otherwise, it computes the result, stores it in the dictionary, and returns it.

Alternatively, we can use a bottom-up dynamic programming approach to generate the Fibonacci numbers in linear time. Here's the implementation:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n

    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[n]

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This version uses a list `fib_sequence` to store the Fibonacci numbers as they are generated. It starts with the first two Fibonacci numbers, `0` and `