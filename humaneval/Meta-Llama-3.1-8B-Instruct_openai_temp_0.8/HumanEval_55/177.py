### Fibonacci Number Calculator
#### Calculating the nth Fibonacci number using memoization for efficient computation.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.
    Starting with 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so forth.

    Args:
        n (int): The position of the Fibonacci number to calculate.

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

    # Create a dictionary to store Fibonacci numbers as they are calculated
    memo = {0: 0, 1: 1}

    # Define a helper function to perform the actual calculation
    def fib_helper(k: int) -> int:
        # If the Fibonacci number is already in the memo dictionary, return it
        if k in memo:
            return memo[k]
        # Otherwise, calculate the Fibonacci number and store it in the memo dictionary
        else:
            result = fib_helper(k - 1) + fib_helper(k - 2)
            memo[k] = result
            return result

    # Call the helper function with the desired Fibonacci number
    return fib_helper(n)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses memoization to efficiently calculate the nth Fibonacci number. The `fib` function stores previously calculated Fibonacci numbers in a dictionary called `memo` to avoid redundant calculations. The `fib_helper` function performs the actual calculation, and the `fib` function calls `fib_helper` with the desired Fibonacci number.