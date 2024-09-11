### Fibonacci Number Calculator
#### Using Memoization for Efficient Computation

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.
    
    Args:
    n (int): Position of the Fibonacci number to calculate.
    
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
    memo = {0: 0, 1: 1}  # Initialize a dictionary for memoization
    
    def fib_helper(k: int) -> int:
        # If the Fibonacci number is already in the dictionary, return it
        if k in memo:
            return memo[k]
        # Otherwise, calculate it and store it in the dictionary
        else:
            result = fib_helper(k - 1) + fib_helper(k - 2)
            memo[k] = result
            return result
    
    return fib_helper(n)

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses a recursive approach with memoization to calculate the n-th Fibonacci number efficiently. The `fib_helper` function is a helper function that uses recursion to calculate the Fibonacci numbers and stores them in a dictionary (`memo`) to avoid redundant calculations.