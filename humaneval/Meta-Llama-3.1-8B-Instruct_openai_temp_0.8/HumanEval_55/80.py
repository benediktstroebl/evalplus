```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    Example:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Test the function
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```

However, this recursive approach is not efficient for large n due to repeated computation. We can improve it using memoization:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    Example:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        memo = {1: 1, 2: 1}
        return fib_helper(n, memo)


def fib_helper(n: int, memo: dict) -> int:
    if n in memo:
        return memo[n]
    else:
        result = fib_helper(n-1, memo) + fib_helper(n-2, memo)
        memo[n] = result
        return result


# Test the function
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```

And for an iterative approach without recursion or recursion with memoization:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    Example:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


# Test the function
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```
This approach is more efficient than the previous recursive approaches as it avoids repeated computation