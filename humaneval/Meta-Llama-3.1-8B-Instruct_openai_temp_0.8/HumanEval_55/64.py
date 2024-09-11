### Fibonacci Number Calculator
```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.
    Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so forth.

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
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
```
This script defines a function `fib(n)` that calculates the `n`-th Fibonacci number. It uses an iterative approach to calculate the Fibonacci numbers, which is more efficient than a recursive approach for larger values of `n`. The function returns the Fibonacci number as an integer. If the input is not a positive integer, it returns an error message.