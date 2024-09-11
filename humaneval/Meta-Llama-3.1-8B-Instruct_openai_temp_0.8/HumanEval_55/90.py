### Fibonacci Number Calculator
#### Python Implementation

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers,
    starting with 1 and 1.
    
    Args:
    n (int): The position of the Fibonacci number to be generated.
    
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
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script defines a function `fib(n)` that calculates the n-th Fibonacci number using an iterative approach. It first checks if `n` is less than or equal to 0 and raises a `ValueError` if it is. Then, it checks for the base cases where `n` is 1 or 2 and returns 1 in both cases. For `n` greater than 2, it initializes two variables `a` and `b` to 1, then iteratively calculates the next Fibonacci number by updating `a` and `b` to `b` and `a + b`, respectively. Finally, it returns the `n`-th Fibonacci number. The script includes docstrings and example usage to demonstrate the function's behavior.