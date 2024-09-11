### Fibonacci Number Generator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

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
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Example usage:
for i in range(1, 11):
    print(f"Fibonacci number at position {i}: {fib(i)}")
```
This script defines a recursive `fib` function that calculates the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function uses recursion to compute the nth number in the sequence. 

The function also handles edge cases where `n` is less than or equal to 1, returning `n` directly.

The script includes an example usage section that generates the first 10 Fibonacci numbers and prints them to the console.

Please note that the recursive approach can be inefficient for large values of `n` due to repeated function calls. A more efficient approach would use dynamic programming or memoization to store and reuse previously computed Fibonacci numbers. 

Here's how you could optimize the function using memoization:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

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
    memo = {0: 0, 1: 1}
    def fib_recursive(k):
        if k not in memo:
            memo[k] = fib_recursive(k-1) + fib_recursive(k-2)
        return memo[k]
    return fib_recursive(n)

# Example usage:
for i in range(1, 11):
    print(f"Fibonacci number at position {i}: {fib(i)}")
```