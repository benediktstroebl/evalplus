### Fibonacci Number Calculation
#### Using Memoization for Efficient Computation

Here's a Python script that calculates the n-th Fibonacci number using memoization for efficient computation:

```python
def fib(n: int, memo={}):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.
        memo (dict, optional): A dictionary used for memoization. Defaults to {}.

    Returns:
        int: The n-th Fibonacci number.
    """
    # Base cases
    if n <= 1:
        return n
    
    # Check if the Fibonacci number is already in the memo dictionary
    if n in memo:
        return memo[n]
    
    # Calculate the Fibonacci number and store it in the memo dictionary
    result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    
    return result

# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses a recursive approach with memoization to calculate the n-th Fibonacci number. The `memo` dictionary stores previously computed Fibonacci numbers to avoid redundant calculations.