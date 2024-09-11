### Fibonacci Number Calculator
#### Python Implementation
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.
    Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so forth.

    :param n: The position of the Fibonacci number to calculate.
    :return: The n-th Fibonacci number.
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

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This Python script defines a function `fib(n)` that calculates the n-th Fibonacci number using an iterative approach. The function starts with `a = 1` and `b = 1` for the base cases of `n = 1` and `n = 2`, then enters a loop to calculate the Fibonacci numbers iteratively, storing the last two calculated numbers in `a` and `b` to use in the next iteration. Finally, it returns the n-th Fibonacci number. The function includes docstrings to describe its purpose, parameters, and return value, as well as example usage.