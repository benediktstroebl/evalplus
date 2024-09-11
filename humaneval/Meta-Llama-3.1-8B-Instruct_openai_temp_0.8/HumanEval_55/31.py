```python
# Define a recursive function to calculate the n-th Fibonacci number
def fib(n: int):
    """
    Return n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Base cases: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fib(n-1) + fib(n-2)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, please note that the given recursive approach has an exponential time complexity due to repeated function calls. For larger values of `n`, a more efficient approach would be to use dynamic programming to store the results of previously computed Fibonacci numbers.

Here's an example of a more efficient dynamic programming approach:

```python
# Define an iterative function to calculate the n-th Fibonacci number using dynamic programming
def fib(n: int):
    """
    Return n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        # Calculate the next Fibonacci number as the sum of the previous two
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence[n]


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This dynamic programming approach has a linear time complexity, making it more suitable for larger values of `n`.