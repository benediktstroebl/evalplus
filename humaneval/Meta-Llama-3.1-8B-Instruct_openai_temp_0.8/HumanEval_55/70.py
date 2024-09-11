### Fibonacci Sequence Generator
#### A Python Script to Generate the N-th Fibonacci Number

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, 
    usually starting with 0 and 1.

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

    # Base cases for the Fibonacci sequence
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1
        
        # Generate Fibonacci numbers up to the n-th number
        for _ in range(2, n + 1):
            # Calculate the next Fibonacci number as the sum of the previous two
            a, b = b, a + b
        
        # Return the n-th Fibonacci number
        return b

# Test the fib function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This Python script defines a function `fib(n)` that returns the n-th Fibonacci number. It uses an iterative approach to calculate the Fibonacci sequence, starting from the base cases `n = 0` and `n = 1`. For `n > 1`, it initializes the first two Fibonacci numbers `a` and `b`, then iteratively calculates the next Fibonacci number as the sum of the previous two, until it reaches the n-th number. The function returns the n-th Fibonacci number.