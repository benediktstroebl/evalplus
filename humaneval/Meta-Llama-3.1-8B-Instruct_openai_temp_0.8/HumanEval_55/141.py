### Fibonacci Number Calculation
#### Self-Contained Python Script
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

    Args:
        n (int): Position of the Fibonacci number to be calculated.

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


# Example usage:
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci({i}) = {fib(i)}")
```
This Python script defines a function `fib(n)` that calculates the n-th Fibonacci number using an iterative approach. The script also includes example usage and a docstring that provides documentation and usage examples.