### Fibonacci Number Generator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

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
    else:
        return fib(n-1) + fib(n-2)


# Example usage:
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

**Note:** This script uses a recursive approach to generate the Fibonacci numbers, which is straightforward but may not be efficient for large values of `n` due to repeated calculations.

If you need a more efficient solution, you can use dynamic programming to store the previously calculated numbers, like this:

```python
def fib(n: int) -> int:
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
        fib_numbers = [0, 1]
        for i in range(2, n):
            fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
        return fib_numbers[-1]


# Example usage:
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This version of the function uses a list to store the previously calculated Fibonacci numbers, which makes it much more efficient for large values of `n`.