### Fibonacci Number Calculator
#### Problem Statement

Write a Python function to calculate the `n`-th Fibonacci number.

#### Solution

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is defined recursively as:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The n-th Fibonacci number.

    Examples:
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

However, the above recursive solution has an exponential time complexity due to repeated function calls. We can improve it by using an iterative approach with constant time complexity.

#### Optimized Solution (Iterative)

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The n-th Fibonacci number.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n <= 1:
        return n

    fib_prev = 0
    fib_curr = 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This optimized solution uses a constant amount of space and has a linear time complexity, making it more efficient than the original recursive solution.