### Fibonacci Number Generator
#### Problem Statement: Calculate the n-th Fibonacci number.

Below is a Python function that uses dynamic programming to efficiently calculate the n-th Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): Index of the Fibonacci number to calculate.

    Returns:
    int: The n-th Fibonacci number.

    Example:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    
    # Handle edge cases where n is less than or equal to 1
    if n <= 1:
        return n
    
    # Initialize a list to store Fibonacci numbers
    fib_numbers = [0, 1]
    
    # Use dynamic programming to calculate Fibonacci numbers up to n
    for i in range(2, n + 1):
        # Calculate the next Fibonacci number as the sum of the two preceding ones
        next_fib = fib_numbers[i - 1] + fib_numbers[i - 2]
        fib_numbers.append(next_fib)
    
    # Return the n-th Fibonacci number
    return fib_numbers[n]


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a function `fib(n)` that calculates the n-th Fibonacci number using dynamic programming. The function creates a list `fib_numbers` to store Fibonacci numbers and iteratively calculates each number as the sum of the two preceding ones. Finally, it returns the n-th Fibonacci number.

The provided example usage demonstrates how to call the `fib(n)` function to calculate Fibonacci numbers for different values of `n`.