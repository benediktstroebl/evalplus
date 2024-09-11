### Fibonacci Number Function
```python
def fib(n: int):
    """Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to return.

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


# Test the function
if __name__ == "__main__":
    test_cases = [1, 2, 8, 10]
    for n in test_cases:
        print(f"Fibonacci number at position {n} is: {fib(n)}")
```

### Explanation
This Python script implements a function called `fib` that returns the n-th Fibonacci number. The Fibonacci sequence is defined as:

- F(1) = F(2) = 1
- F(n) = F(n-1) + F(n-2) for n > 2

The `fib` function uses a loop to calculate the n-th Fibonacci number. It starts with `a = 1` and `b = 1`, then iteratively updates `a` and `b` to be `b` and `a + b`, respectively. This process is repeated until `b` is the n-th Fibonacci number.