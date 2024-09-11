### Fibonacci Number Calculation

Here's a Python script that calculates the n-th Fibonacci number.
#### Using Memoization for Efficient Calculation

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to be calculated.

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
    memo = {0: 0, 1: 1}  # Store Fibonacci numbers from 0 to 1 in the memo dictionary
    def fib_helper(k: int) -> int:
        """
        Recursive helper function to calculate the k-th Fibonacci number.
        """
        if k not in memo:  # If the k-th Fibonacci number is not in the memo dictionary
            memo[k] = fib_helper(k-1) + fib_helper(k-2)  # Calculate it and store it in the memo dictionary
        return memo[k]
    return fib_helper(n)

# Test the fib function
print(fib(10))
print(fib(1))
print(fib(8))
```

In this code, we use a technique called memoization to store the calculated Fibonacci numbers in a dictionary. This way, if we need to calculate the same Fibonacci number again, we can simply retrieve it from the dictionary instead of recalculating it. This makes the function much more efficient, especially for large values of n.

When you run this script, it will print the 10th, 1st, and 8th Fibonacci numbers.