### Fibonacci Number Calculator
#### Using Recursion and Memoization for Efficiency

```python
def fib(n: int, memo: dict = {}) -> int:
    """
    Return n-th Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to return.
    memo (dict): A dictionary to store previously calculated Fibonacci numbers.
    
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
    
    # Base cases
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    
    # Recursive case
    result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result  # Store the result in the memo dictionary
    
    return result

# Example use cases
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Fibonacci number at position {n}: {fib(n)}")
```

This script defines a function `fib` that calculates the n-th Fibonacci number using recursion and memoization for efficiency. The `memo` dictionary stores previously calculated Fibonacci numbers to avoid redundant calculations. The script also includes example use cases to demonstrate its usage.