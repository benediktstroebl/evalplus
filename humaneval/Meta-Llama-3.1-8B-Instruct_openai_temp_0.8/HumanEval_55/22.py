```markdown
**Fibonacci Number Generator**
================================

### Problem Description

The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

### Solution

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to be generated.

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
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Example usage:
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
    print(fib(-5))  # Output: Input should be a positive integer.
```

### Explanation

This Python function uses an iterative approach to calculate the n-th Fibonacci number. It handles the base cases where `n` is less than or equal to 0, and directly returns the first and second Fibonacci numbers. For `n` greater than 2, it initializes the first two Fibonacci numbers (`a` and `b`) as 1 and then iteratively calculates the subsequent numbers by updating `a` and `b` using the formula `b = a + b`. Finally, it returns the `n`-th Fibonacci number.

This solution provides a simple and efficient way to generate Fibonacci numbers for large values of `n`.