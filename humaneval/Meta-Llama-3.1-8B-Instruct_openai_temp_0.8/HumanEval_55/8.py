Here is a Python function that calculates the nth Fibonacci number using recursion. This is not the most efficient way to calculate Fibonacci numbers but it is a simple and easily understandable way.

```markdown
### Fibonacci Number Calculation using Recursion
#### This code defines a function to calculate the nth Fibonacci number.

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.
    
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
    # Base cases
    if n <= 1:
        return n
    # Recursive case
    else:
        return fib(n-1) + fib(n-2)


# Test the function
print(fib(10))
print(fib(1))
print(fib(8))
```

However, this recursive approach has a time complexity of O(2^n) which is inefficient for large values of n. The reason for this is because the function is recalculating the same Fibonacci numbers multiple times.

Here is an iterative version of the function which calculates the nth Fibonacci number in O(n) time complexity.

```markdown
### Fibonacci Number Calculation using Iteration
#### This code defines a function to calculate the nth Fibonacci number using iteration.

```python
def fib(n: int):
    """
    Return n-th Fibonacci number.
    
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
    # Base case
    if n <= 1:
        return n
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Calculate the nth Fibonacci number
    for _ in range(2, n+1):
        a, b = b, a + b
    
    return b


# Test the function
print(fib(10))
print(fib(1))
print(fib(8))
```
This iterative version maintains an accumulator for the last two Fibonacci numbers, which allows it to calculate the nth Fibonacci number in O(n) time.