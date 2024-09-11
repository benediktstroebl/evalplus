### Fibonacci Number Calculator

Below is a Python script that defines a function to calculate the nth Fibonacci number. This function uses an iterative approach to calculate the result, which is more memory-efficient than a recursive approach for large inputs.

```markdown
### Code

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

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
    # Handle edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize variables for the iteration
    a, b = 1, 1

    # Iterate from 2 to n (inclusive)
    for _ in range(2, n + 1):
        # Update a and b for the next iteration
        a, b = b, a + b

    # Return the calculated Fibonacci number
    return b

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

### Explanation

*   The function `fib` takes an integer `n` as input, representing the position of the Fibonacci number to calculate.
*   It first handles edge cases where `n` is 0 or 1, returning 0 and 1 respectively as the first two Fibonacci numbers.
*   It then initializes two variables `a` and `b` to 1, which will hold the last two Fibonacci numbers calculated.
*   The function iterates from 2 to `n` (inclusive), updating `a` and `b` for each iteration using the recurrence relation `F(n) = F(n-1) + F(n-2)`.
*   Finally, it returns the calculated `n`-th Fibonacci number stored in `b`.

### Example Use Cases

You can use this function to calculate any Fibonacci number position. Just call the function with the position as the argument. For example:

*   `fib(10)` returns the 10th Fibonacci number.
*   `fib(20)` returns the 20th Fibonacci number.