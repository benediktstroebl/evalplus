```python
def fib(n: int):
    """
    Return n-th Fibonacci number.
    
    This function uses memoization to store previously calculated Fibonacci numbers.
    This technique avoids redundant calculations and improves performance for large inputs.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.
    """
    # Initialize a dictionary to store memoized Fibonacci numbers
    memo = {0: 0, 1: 1}

    def fib_helper(k: int) -> int:
        # If the Fibonacci number is already memoized, return it
        if k in memo:
            return memo[k]
        # Otherwise, calculate the Fibonacci number recursively and store it in memo
        else:
            result = fib_helper(k - 1) + fib_helper(k - 2)
            memo[k] = result
            return result

    # Return the n-th Fibonacci number
    return fib_helper(n)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses a recursive approach with memoization to efficiently calculate Fibonacci numbers. The `fib` function initializes a dictionary `memo` to store previously calculated Fibonacci numbers, and a nested `fib_helper` function performs the recursive calculations. This implementation ensures that each Fibonacci number is calculated only once, even for large inputs.