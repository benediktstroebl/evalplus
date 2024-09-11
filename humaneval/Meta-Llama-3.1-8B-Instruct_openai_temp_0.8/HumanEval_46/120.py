### Fib4 Number Sequence Calculator
```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.

    Args:
        n (int): The index of the element in the fib4 number sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # Base cases
        a, b, c, d = 0, 0, 2, 0
        # Compute fib4(n) using dynamic programming
        for i in range(4, n + 1):
            fib4_n = a + b + c + d
            a, b, c, d = b, c, d, fib4_n
        return fib4_n


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script defines a function `fib4(n)` that uses dynamic programming to efficiently compute the n-th element of the fib4 number sequence. The function takes an integer `n` as input and returns the corresponding element in the sequence. The script also includes test cases to demonstrate the correctness of the function.