### Fibonacci Number Calculation

Below is a Python script that defines a function `fib` to calculate the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number to be calculated.

    Returns:
        int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        # Base cases
        return n
    else:
        # Recursive case
        return fib(n-1) + fib(n-2)


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i} is: {fib(i)}")
```

### Explanation

*   The function `fib(n)` uses a recursive approach to calculate the n-th Fibonacci number.
*   If `n` is less than or equal to 1, it returns `n` as the base case.
*   For any other `n`, it calls itself with `n-1` and `n-2` and returns the sum of these two calls to calculate the n-th Fibonacci number.
*   The script then tests the function by printing the Fibonacci numbers from position 1 to 10.

### Advice

*   This recursive implementation is straightforward but may lead to performance issues for large values of `n` due to repeated calculations.
*   For a more efficient solution, consider using an iterative approach or memoization to store and reuse previously calculated Fibonacci numbers.