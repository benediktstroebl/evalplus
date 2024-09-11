### Fibonacci Function
#### Recursive Implementation

Here is a simple recursive implementation of the Fibonacci function in Python:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, please note that this is not the most efficient solution for large values of `n`. This is because it does a lot of repeated work (calculating the same Fibonacci numbers over and over again). 

#### Iterative Implementation

A more efficient solution is to use an iterative approach:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr

    return curr

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This solution has a time complexity of O(n) and a space complexity of O(1), making it much more efficient for large values of `n`.