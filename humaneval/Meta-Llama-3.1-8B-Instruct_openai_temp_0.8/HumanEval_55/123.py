```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    """
    # Base cases: F(1) = F(2) = 1
    if n <= 2:
        return 1
    
    # Initialize variables to store the previous two Fibonacci numbers
    a, b = 1, 1
    
    # Calculate the n-th Fibonacci number
    for _ in range(3, n + 1):
        # Update the previous two Fibonacci numbers
        a, b = b, a + b
    
    # Return the n-th Fibonacci number
    return b

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a function `fib(n)` that calculates the n-th Fibonacci number. It uses an iterative approach to avoid recursion and improve performance. The function handles base cases (n <= 2) and returns the correct result for larger values of n. The example usage at the end demonstrates how to call the function with different inputs.