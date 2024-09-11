### Fibonacci Number Calculation
#### Using Recursive and Iterative Methods

```python
def fib_recursive(n: int) -> int:
    """Return n-th Fibonacci number using recursion.
    
    Args:
    n (int): The position of the Fibonacci number to be calculated.
    
    Returns:
    int: The n-th Fibonacci number.
    
    Raises:
    ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """Return n-th Fibonacci number using iteration.
    
    Args:
    n (int): The position of the Fibonacci number to be calculated.
    
    Returns:
    int: The n-th Fibonacci number.
    
    Raises:
    ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n <= 1:
        return n
    
    fib_prev, fib_curr = 0, 1
    for _ in range(2, n + 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    
    return fib_curr


def fib_memoization(n: int) -> int:
    """Return n-th Fibonacci number using memoization.
    
    Args:
    n (int): The position of the Fibonacci number to be calculated.
    
    Returns:
    int: The n-th Fibonacci number.
    
    Raises:
    ValueError: If n is a negative integer.
    """
    memo = {0: 0, 1: 1}
    
    def fib_helper(k: int) -> int:
        if k not in memo:
            memo[k] = fib_helper(k-1) + fib_helper(k-2)
        return memo[k]
    
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    return fib_helper(n)


# Example usage
if __name__ == "__main__":
    print(fib_recursive(10))  # Output: 55
    print(fib_iterative(10))  # Output: 55
    print(fib_memoization(10))  # Output: 55
```

This script provides three different methods to calculate the n-th Fibonacci number:

1.  **fib_recursive**: Uses recursive function calls to calculate the Fibonacci number.
2.  **fib_iterative**: Uses a loop to iteratively calculate the Fibonacci number.
3.  **fib_memoization**: Uses memoization to store previously calculated Fibonacci numbers and avoid redundant calculations.

Each method includes input validation to ensure that the input is a non-negative integer. The example usage demonstrates how to call these functions with `n = 10` to calculate the 10th Fibonacci number.