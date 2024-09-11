### Fibonacci Number Calculation

The following Python script calculates the `n`-th Fibonacci number using memoization for efficient computation.

```python
def fib(n: int, memo: dict = {}) -> int:
    """
    Return n-th Fibonacci number.
    
    Args:
    n (int): Position of the Fibonacci number to calculate.
    memo (dict): Dictionary to store previously calculated Fibonacci numbers.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    
    # Base cases: Fibonacci numbers are 1 for positions 0 and 1
    if n <= 1:
        return n
    
    # Check if the Fibonacci number is already calculated and stored in the memo
    if n in memo:
        return memo[n]
    
    # Calculate the Fibonacci number using memoization
    result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result  # Store the calculated Fibonacci number in the memo
    
    return result

# Test cases
print(fib(10))  # Expected output: 55
print(fib(1))   # Expected output: 1
print(fib(8))   # Expected output: 21
```

This script defines a `fib` function that takes an integer `n` and an optional dictionary `memo` to store previously calculated Fibonacci numbers. It uses recursion with memoization to efficiently calculate the `n`-th Fibonacci number. The memo is used to store the calculated Fibonacci numbers, allowing the function to avoid redundant calculations and improve performance for larger values of `n`.