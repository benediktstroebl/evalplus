### Fibonacci Number Generator
#### Using Memoization to Optimize Calculation

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    
    # Create a dictionary to store previously calculated Fibonacci numbers
    memo = {0: 0, 1: 1}
    
    # Function to calculate the nth Fibonacci number using memoization
    def fib_helper(k):
        if k not in memo:
            memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]
    
    return fib_helper(n)

# Test the function
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```

This script uses memoization to optimize the calculation of Fibonacci numbers. Memoization is a technique where the results of expensive function calls are cached and reused to avoid recalculating the same values repeatedly. In this case, we use a dictionary to store the Fibonacci numbers as they are calculated, allowing us to return the cached result instead of recalculating it. This significantly improves the performance of the function for large values of `n`.