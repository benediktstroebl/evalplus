### Fibonacci Number Generator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number.

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
    return fib(n - 1) + fib(n - 2)


# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```
This script defines a recursive function `fib(n)` to calculate the n-th Fibonacci number. Note that this implementation uses recursion, which can be inefficient for large values of `n` due to repeated calculations. A more efficient approach would be to use dynamic programming to store previously calculated Fibonacci numbers.

Alternatively, you can use an iterative approach to calculate Fibonacci numbers more efficiently:
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number.

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
    fib_prev, fib_curr = 0, 1
    for _ in range(2, n + 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    return fib_curr


# Example usage
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```
This iterative version of the `fib(n)` function has a time complexity of O(n), making it more efficient for large values of `n`.