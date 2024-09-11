### Fibonacci Number Calculator
#### Fib Function Implementation
```python
def fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The n-th Fibonacci number.

    Example:
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
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
    try:
        print(fib(-5))  # Raises ValueError
    except ValueError as e:
        print(e)
```
This script defines a `fib` function that calculates the n-th Fibonacci number using a simple iterative approach. It also includes example usage and error handling for invalid inputs. The script is self-contained and easy to run.