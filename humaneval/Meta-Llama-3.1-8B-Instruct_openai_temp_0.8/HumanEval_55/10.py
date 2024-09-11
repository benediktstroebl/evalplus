### Fibonacci Number Generator
#### Problem Description

The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, usually starting with 0 and 1.

#### Solution
```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

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
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```
#### Explanation

This script defines a function `fib` that takes an integer `n` as input and returns the `n`-th Fibonacci number. The function uses a simple iterative approach to calculate the Fibonacci number.

- For `n <= 0`, it raises a `ValueError` as the input must be a positive integer.
- For `n == 1` or `n == 2`, it returns 1 as these are the base cases of the Fibonacci sequence.
- For `n > 2`, it uses a loop to calculate the Fibonacci number. It initializes `a` and `b` to 1, then iterates from `2` to `n`, updating `a` and `b` at each step to the next two numbers in the sequence. Finally, it returns `b` as the `n`-th Fibonacci number.

The script also includes example usage at the end to demonstrate how to use the `fib` function.