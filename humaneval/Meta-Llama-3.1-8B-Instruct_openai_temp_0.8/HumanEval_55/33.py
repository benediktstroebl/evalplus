### Fibonacci Number Calculation

The following Python script provides a function to calculate the `n`-th Fibonacci number using dynamic programming.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to be calculated.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    fib_values = [0, 1]
    for i in range(2, n + 1):
        fib_values.append(fib_values[i-1] + fib_values[i-2])
    return fib_values[n]

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, for larger inputs, the above script can be inefficient due to repeated calculations. We can optimize it using memoization to store previously calculated Fibonacci numbers.

### Optimized Fibonacci Calculation

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to be calculated.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    
    # Initialize a dictionary to store memoized values
    memo = {0: 0, 1: 1}
    
    def fib_recursive(k: int) -> int:
        if k not in memo:
            memo[k] = fib_recursive(k-1) + fib_recursive(k-2)
        return memo[k]
    
    return fib_recursive(n)

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This optimized version reduces the time complexity from exponential to linear by avoiding redundant calculations.