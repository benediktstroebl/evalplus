### Fibonacci Number Calculation
#### Overview

This script calculates the n-th Fibonacci number using a recursive approach.

#### Code
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): Position of the Fibonacci number.

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
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Test cases
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```
#### Notes

*   This recursive approach is not efficient for large values of `n` due to redundant calculations.
*   For a more efficient solution, consider using dynamic programming techniques like memoization or bottom-up approach.
*   In a real-world scenario, you might want to add error handling for invalid inputs (e.g., negative numbers).