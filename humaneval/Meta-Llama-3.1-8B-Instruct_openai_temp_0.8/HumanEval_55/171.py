### Fibonacci Number Calculation
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    :param n: Number of Fibonacci sequence to calculate.
    :return: The n-th Fibonacci number.
    """
    if n <= 1:
        # Base cases: Fib(0) = 0, Fib(1) = 1
        return n
    else:
        # Recursive case: Fib(n) = Fib(n-1) + Fib(n-2)
        return fib(n-1) + fib(n-2)


# Test the function
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```
This Python script defines a recursive function `fib` that calculates the `n`-th Fibonacci number. It handles base cases (Fibonacci numbers 0 and 1) and uses recursive calls for larger values of `n`. The `if __name__ == "__main__":` block includes test cases to demonstrate the function's correctness.

**Note:** This recursive solution is not the most efficient way to calculate Fibonacci numbers for large `n`. A more efficient approach would use dynamic programming or memoization to store previously calculated values and avoid redundant calculations. However, the recursive solution is simple and illustrative.