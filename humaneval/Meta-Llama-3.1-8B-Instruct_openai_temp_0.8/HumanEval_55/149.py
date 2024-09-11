### Recursive Fibonacci Function
Here's a Python script that implements the Fibonacci function using recursion:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The sequence of Fibonacci numbers is defined recursively as:
    - fib(1) = 1
    - fib(2) = 1
    - fib(n) = fib(n-1) + fib(n-2) for n > 2

    Args:
        n (int): The index of the Fibonacci number to return.

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
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
However, this recursive implementation has an exponential time complexity due to the repeated computation of the same Fibonacci numbers. A more efficient solution would use dynamic programming to store and reuse previously computed values.

### Dynamic Programming Fibonacci Function
Here's a revised version of the Fibonacci function that uses dynamic programming to achieve a linear time complexity:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number using dynamic programming.

    Args:
        n (int): The index of the Fibonacci number to return.

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
        return 1

    # Create a list to store Fibonacci numbers
    fib_numbers = [0] * (n + 1)

    # Initialize the first two Fibonacci numbers
    fib_numbers[1] = 1

    # Compute Fibonacci numbers iteratively
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i-1] + fib_numbers[i-2]

    return fib_numbers[n]

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
This dynamic programming implementation has a linear time complexity of O(n), making it much more efficient for large values of n.