### Fibonacci Number Generator
#### Python Implementation

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

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
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

### Explanation

*   The function `fib(n)` calculates the n-th Fibonacci number using an iterative approach.
*   It first checks for invalid inputs (n <= 0) and raises a `ValueError` accordingly.
*   For n = 1, it returns 1 since it's the base case of the Fibonacci sequence.
*   For n > 1, it uses a loop to generate the Fibonacci numbers iteratively. It starts with a = 1 and b = 1, and then updates a and b in each iteration to be the previous value of b and the sum of the previous a and b, respectively.
*   The function returns the last calculated Fibonacci number, which corresponds to the n-th number in the sequence.

### Time Complexity

*   The time complexity of this implementation is O(n), where n is the input number. This is because the loop runs n-1 times to calculate the n-th Fibonacci number.