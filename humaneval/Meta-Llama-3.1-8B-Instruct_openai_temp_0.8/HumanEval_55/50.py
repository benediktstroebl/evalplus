### Fibonacci Number Calculator

Below is a Python script that calculates the n-th Fibonacci number using a recursive function.

```python
def fib(n: int):
    """Return n-th Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number to be calculated.
    
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
        return fib(n-1) + fib(n-2)


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This script calculates the n-th Fibonacci number by recursively summing the two preceding ones. However, please note that this approach is inefficient for large values of n due to repeated computation.

Alternatively, you can use an iterative solution for better performance:

```python
def fib(n: int):
    """Return n-th Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number to be calculated.
    
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
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    
    return b


# Test the function
if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci number at position {i}: {fib(i)}")
```

This iterative solution directly calculates the n-th Fibonacci number without repeated computation, making it more efficient for large values of n.