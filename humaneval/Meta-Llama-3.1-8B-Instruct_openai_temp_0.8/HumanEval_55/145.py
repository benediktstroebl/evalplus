### Fibonacci Number Generator
#### Using Memoization for Efficient Computation

Here's a Python script that uses memoization for efficient computation of Fibonacci numbers.

```python
def fib(n: int, memo: dict = {}):
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Index of the Fibonacci number to compute.
        memo (dict, optional): Dictionary to store computed Fibonacci numbers. Defaults to {}.

    Returns:
        int: n-th Fibonacci number.
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


# Example usage:
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at index {i}: {fib(i)}")
```

This script uses a dictionary `memo` to store computed Fibonacci numbers. If the `n`-th Fibonacci number has already been computed, it simply returns the stored result. Otherwise, it recursively computes the `n`-th Fibonacci number and stores it in the `memo` dictionary for future use. This approach significantly improves performance by avoiding redundant computations.