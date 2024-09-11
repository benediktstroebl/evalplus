### Fibonacci Number Calculation
#### A Python Function to Calculate Fibonacci Numbers

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

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
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        # Initialize the first two numbers in the Fibonacci sequence
        a, b = 1, 1
        
        # Calculate the n-th Fibonacci number
        for _ in range(2, n):
            a, b = b, a + b
        
        return b

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This Python function uses a simple iterative approach to calculate the n-th Fibonacci number. It starts with the first two numbers in the sequence (1 and 1) and then iteratively calculates the next number as the sum of the previous two. The function handles edge cases where n is less than or equal to 0 by raising a ValueError.