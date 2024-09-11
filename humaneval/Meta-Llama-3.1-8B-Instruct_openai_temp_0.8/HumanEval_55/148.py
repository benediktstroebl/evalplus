### Fibonacci Number Calculator
#### Python Script
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to return.

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
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(1))   # Output: 1
    print(fib(8))   # Output: 21
```
This Python script defines a function `fib` that calculates the n-th Fibonacci number using an iterative approach. The function takes an integer `n` as input and returns the n-th Fibonacci number.

The function starts by checking if `n` is less than or equal to 1, in which case it returns `n` directly. Otherwise, it initializes two variables `a` and `b` to 0 and 1, respectively. The function then enters a loop that iterates from 2 to `n` (inclusive), updating `a` and `b` at each iteration using the recurrence relation of the Fibonacci sequence. Finally, the function returns the value of `b`, which is the n-th Fibonacci number.

For testing purposes, the script includes a guard clause `if __name__ == "__main__":` that ensures the test cases are executed only when the script is run directly (i.e., not when it is imported as a module by another script).