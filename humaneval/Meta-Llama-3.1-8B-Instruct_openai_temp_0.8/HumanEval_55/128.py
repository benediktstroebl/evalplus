### Fibonacci Number Generator
#### A Python Script to Calculate the nth Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to be generated.

    Returns:
        int: The nth Fibonacci number.

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

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
print(fib(0))   # Output: Input should be a positive integer.
```

This Python script uses an iterative approach to calculate the nth Fibonacci number. It handles edge cases where n is less than or equal to 0 and returns the correct Fibonacci numbers for n = 1, 2, and other positive integers. The example use cases demonstrate how to use the function to generate Fibonacci numbers.