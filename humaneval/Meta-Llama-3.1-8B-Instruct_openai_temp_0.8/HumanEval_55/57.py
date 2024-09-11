### Fibonacci Number Generator
#### Recursive Solution

Below is a Python function that uses recursion to calculate the nth Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to be calculated.

    Returns:
        int: The nth Fibonacci number.

    Example:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    # Base cases for recursion
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        # Recursive case: fib(n) = fib(n-1) + fib(n-2)
        return fib(n-1) + fib(n-2)

# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

#### Iterative Solution

Below is a Python function that uses iteration to calculate the nth Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to be calculated.

    Returns:
        int: The nth Fibonacci number.

    Example:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    # Base case for iteration
    if n == 1:
        return 1

    # Initialize variables for iteration
    a, b = 1, 1

    # Iterate from n=3 to n
    for _ in range(3, n + 1):
        # Update a and b for the next iteration
        a, b = b, a + b

    # Return the nth Fibonacci number
    return b

# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
Note that the iterative solution is computationally more efficient than the recursive solution for large values of n due to its reduced computational overhead and memory usage.