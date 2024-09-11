### Fibonacci Number Generator

This Python script uses a recursive approach to calculate the nth Fibonacci number. However, a more efficient solution would be to use dynamic programming to avoid redundant calculations.

```python
def fib_recursive(n: int):
    """Return n-th Fibonacci number using recursion.
    
    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib_recursive(10)
    55
    >>> fib_recursive(1)
    1
    >>> fib_recursive(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int):
    """Return n-th Fibonacci number using iteration.
    
    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib_iterative(10)
    55
    >>> fib_iterative(1)
    1
    >>> fib_iterative(8)
    21
    """
    fib_prev = 0
    fib_curr = 1

    if n == 1:
        return fib_prev
    elif n == 2:
        return fib_curr

    for _ in range(2, n):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr


def fib_dp(n: int):
    """Return n-th Fibonacci number using dynamic programming.
    
    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib_dp(10)
    55
    >>> fib_dp(1)
    1
    >>> fib_dp(8)
    21
    """
    fib_values = [0, 1] + [0] * (n - 1)

    if n > 1:
        for i in range(2, n + 1):
            fib_values[i] = fib_values[i - 1] + fib_values[i - 2]

    return fib_values[n]


# Example usage:
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Fibonacci({n}) = {fib_recursive(n)}")
        print(f"Fibonacci({n}) = {fib_iterative(n)}")
        print(f"Fibonacci({n}) = {fib_dp(n)}")
        print()
```

This script defines three functions to calculate the nth Fibonacci number: `fib_recursive` using recursion, `fib_iterative` using iteration, and `fib_dp` using dynamic programming. The example usage demonstrates how to use each function.