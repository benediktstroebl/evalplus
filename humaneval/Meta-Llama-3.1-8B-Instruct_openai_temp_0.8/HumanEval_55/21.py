### Fibonacci Number Calculator

Below is a Python script using memoization to efficiently calculate Fibonacci numbers.

```python
def fib(n: int, memo: dict = {}) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to calculate.
    memo (dict, optional): Dictionary to store memoized Fibonacci values. Defaults to {}.

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
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
        memo[n] = result
        return result


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This script uses a dictionary to store previously calculated Fibonacci numbers, allowing it to efficiently calculate larger Fibonacci numbers. The function `fib` takes two arguments: `n` and `memo`. The `n` argument is the position of the Fibonacci number to calculate, and the `memo` dictionary stores memoized Fibonacci values to avoid redundant calculations.

The function first checks if `n` is less than or equal to 0, in which case it returns an error message. If `n` is 1, it returns 1. If `n` is already in the `memo` dictionary, it returns the stored value. Otherwise, it calculates the Fibonacci number by recursively calling itself with `n-1` and `n-2`, adds the results, stores the result in the `memo` dictionary, and returns it.

The script also includes a test case at the end to demonstrate how to use the `fib` function. It calculates and prints the Fibonacci numbers for positions 1 to 10.