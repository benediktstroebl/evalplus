### Python Script to Calculate the nth Fibonacci Number
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number to calculate.

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
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        # Initialize variables to store the previous two Fibonacci numbers
        a, b = 1, 1
        # Calculate the nth Fibonacci number
        for _ in range(2, n):
            # Update the previous two Fibonacci numbers
            a, b = b, a + b
        # Return the nth Fibonacci number
        return b


# Example usage:
if __name__ == "__main__":
    print(f"10th Fibonacci number: {fib(10)}")
    print(f"1st Fibonacci number: {fib(1)}")
    print(f"8th Fibonacci number: {fib(8)}")
```
This script uses an iterative approach to calculate the nth Fibonacci number, which is more efficient than a recursive approach for large values of n.