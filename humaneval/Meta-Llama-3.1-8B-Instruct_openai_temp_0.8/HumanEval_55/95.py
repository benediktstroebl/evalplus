### Fibonacci Number Calculator
#### A Python Script to Calculate the N-th Fibonacci Number

```python
def fib(n: int) -> int:
    """
    This function calculates the n-th Fibonacci number.
    
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
    
    # Base cases for Fibonacci sequence
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    # Initialize variables to store previous two Fibonacci numbers
    a, b = 1, 1
    
    # Calculate the n-th Fibonacci number
    for _ in range(2, n):
        a, b = b, a + b
    
    return b

# Test the function with some examples
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a function `fib(n)` that calculates the n-th Fibonacci number using a simple iterative approach. The function takes an integer `n` as input and returns the corresponding Fibonacci number. The script also includes some test cases to demonstrate the function's correctness.