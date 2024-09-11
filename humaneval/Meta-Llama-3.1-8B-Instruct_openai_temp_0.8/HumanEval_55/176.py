### Fibonacci Number Calculator
#### Python Implementation

Below is a Python script that implements the Fibonacci function using memoization to store previously computed Fibonacci numbers. This approach significantly improves performance for large inputs.

```markdown
def fib(n: int, memo: dict = {}):
    """
    Return n-th Fibonacci number using memoization.

    Args:
    n (int): The position of the Fibonacci number to calculate.
    memo (dict): Dictionary storing previously computed Fibonacci numbers. Defaults to {}.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n in memo:  # Check if Fibonacci number is already computed
        return memo[n]
    if n <= 2:  # Base case: Fibonacci numbers 0 and 1 are 0 and 1 respectively
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)  # Compute Fibonacci number recursively
    return memo[n]

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script defines a `fib` function that calculates the `n-th` Fibonacci number using memoization. The `memo` dictionary stores previously computed Fibonacci numbers to avoid redundant calculations and improve performance. The base case for the recursion is when `n` is less than or equal to 2, where the `n-th` Fibonacci number is defined as 1. For larger values of `n`, the function recursively computes the `n-th` Fibonacci number as the sum of the `(n - 1)-th` and `(n - 2)-th` Fibonacci numbers, which are retrieved from the `memo` dictionary or computed recursively if they are not already stored.