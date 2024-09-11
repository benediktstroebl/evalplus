### Fibonacci Number Calculator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

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
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This script defines a recursive function `fib(n)` that calculates the `n`-th Fibonacci number. It raises a `ValueError` if the input is not a positive integer. The example usage at the end demonstrates how to use the function to calculate the first 10 Fibonacci numbers.

However, please note that the above recursive function may cause a stack overflow for large inputs due to the numerous recursive calls. In such cases, an iterative approach would be more efficient. Here's an alternative version using iteration:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to be calculated.

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
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```