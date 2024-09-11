### Fibonacci Number Generator
#### Problem Statement: Generate the nth Fibonacci number

Below is a Python function that uses recursion to generate the nth Fibonacci number. This function handles edge cases and provides unit tests to ensure correctness.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number to generate.

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

    # Base cases: If n is 1 or 2, return 1
    if n == 1 or n == 2:
        return 1
    # Recursive case: If n is greater than 2, return the sum of the two preceding numbers
    else:
        return fib(n - 1) + fib(n - 2)


# Example usage:
if __name__ == "__main__":
    # Test cases
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34
    assert fib(10) == 55

    # Run test suite
    print("Test suite passed.")
```

Alternatively, you can use an iterative approach to calculate the nth Fibonacci number, which is more efficient than the recursive approach:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number to generate.

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

    # Initialize the first two Fibonacci numbers
    a, b = 1, 1

    # Calculate the nth Fibonacci number
    for _ in range(2, n):
        # Update a and b for the next iteration
        a, b = b, a + b

    return b


# Example usage:
if __name__ == "__main__":
    # Test cases
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34
    assert fib(10) == 55

    # Run test suite
    print("Test suite passed.")
```