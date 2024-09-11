## Fibonacci Number Generator
### A Python Function to Calculate the nth Fibonacci Number

Below is a Python script that uses memoization to efficiently calculate the nth Fibonacci number. Memoization is an optimization technique where we store the results of expensive function calls so that we can reuse them when the same inputs occur again.

```python
def fib(n: int):
    """Return n-th Fibonacci number.
    
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
    # Initialize a dictionary to store Fibonacci numbers
    memo = {0: 0, 1: 1}
    
    def fib_helper(x: int) -> int:
        # If the Fibonacci number is already in the memo dictionary, return it
        if x in memo:
            return memo[x]
        # Otherwise, calculate the Fibonacci number and store it in the memo dictionary
        else:
            result = fib_helper(x-1) + fib_helper(x-2)
            memo[x] = result
            return result
    
    # Use the helper function to calculate the nth Fibonacci number
    return fib_helper(n)

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a function `fib` that takes an integer `n` as input and returns the nth Fibonacci number. The function uses a helper function `fib_helper` that recursively calculates the Fibonacci numbers and stores them in a memo dictionary to avoid redundant calculations. The main function simply calls the helper function with the input `n` and returns the result. The script also includes some example test cases to demonstrate the function's usage.