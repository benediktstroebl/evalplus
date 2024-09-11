Here's a Python script that uses memoization to calculate the n-th Fibonacci number efficiently:
```markdown
### Fibonacci Number Calculator

This script uses memoization to efficiently calculate the n-th Fibonacci number.

#### Code
```python
def fib(n: int, memo: dict = {}):
    """Return n-th Fibonacci number.
    
    Args:
    - n (int): The position of the Fibonacci number to calculate.
    - memo (dict, optional): A dictionary to store previously calculated Fibonacci numbers. Defaults to {}.
    
    Returns:
    - int: The n-th Fibonacci number.
    
    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Check if the Fibonacci number is already in the memo
    elif n not in memo:
        # Calculate the Fibonacci number and store it in the memo
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    # Return the Fibonacci number from the memo
    return memo[n]

# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

#### Explanation

This script uses a recursive approach with memoization to calculate the n-th Fibonacci number efficiently. The `fib` function takes an additional `memo` dictionary to store previously calculated Fibonacci numbers. This allows the function to avoid redundant calculations and reduce the time complexity from exponential to linear.

The base cases are handled first, where `n <= 0` returns 0 and `n == 1` returns 1. If the Fibonacci number is not in the `memo` dictionary, it is calculated recursively and stored in the dictionary. Finally, the Fibonacci number is returned from the `memo` dictionary.

You can run this script in a Python environment to see the example usage.