### Fibonacci Number Generator

Below is a Python script that uses a recursive approach to generate the nth Fibonacci number. The Fibonacci sequence starts with two 1s, and every subsequent number is the sum of the previous two.

```markdown
### Code

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21

```

### Explanation

The script uses a recursive approach to generate the nth Fibonacci number. It checks the input for the following cases:

- If n is less than or equal to 0, it raises a ValueError since the Fibonacci sequence is not defined for non-positive integers.
- If n is 1 or 2, it returns 1 since the first two Fibonacci numbers are 1.
- For n greater than 2, it recursively calls the function with n-1 and n-2 and returns the sum.

Note that this recursive approach can be inefficient for large values of n due to the repeated computation of the same Fibonacci numbers. For a more efficient approach, consider using dynamic programming or memoization.