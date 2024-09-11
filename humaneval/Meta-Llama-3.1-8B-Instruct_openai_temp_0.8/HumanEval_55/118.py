### Fibonacci Number Generator
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is defined as:
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): Position of the Fibonacci number to return.

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


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"F({i}) = {fib(i)}")
```
This script defines a recursive function `fib(n)` that calculates the n-th Fibonacci number according to the Fibonacci sequence's definition. The function uses recursion to build up the Fibonacci sequence from the base cases where F(1) = 1 and F(0) = 0.