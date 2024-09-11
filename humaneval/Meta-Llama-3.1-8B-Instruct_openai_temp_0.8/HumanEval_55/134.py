**Fibonacci Number Generator**
====================================

This Python script calculates the n-th Fibonacci number.

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number to generate.
    
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


# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, the script above uses recursion which can be inefficient for large values of `n` due to the repeated calculations involved. A more efficient approach would be to use dynamic programming to store and reuse intermediate results.

**Efficient Fibonacci Number Generator**
---------------------------------------

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number to generate.
    
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
    
    fib_prev = 0
    fib_curr = 1
    
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    
    return fib_curr


# Example usage
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This version of the function uses a loop to calculate the Fibonacci numbers up to the `n`-th Fibonacci number, avoiding the repeated calculations involved in the recursive approach.