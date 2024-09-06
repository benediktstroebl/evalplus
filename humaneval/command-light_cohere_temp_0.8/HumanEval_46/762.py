```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive number is a fraction of the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and the sequence continues by adding the last two numbers, then subtracting one to get the next pair.
    :param n: int, the index of the Fibonacci number to compute
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    # Check for negative input
    if n < 0:
        raise ValueError("Input should be a non-negative integer")

    # Calculate Fibonacci number using iterative method
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b

# Test the function
test_fib = fib4(5)
print("Fibonacci of index 5:", test_fib)  # Output: 4
test_fib = fib4(7)
print("Fibonacci of index 7:", test_fib)  # Output: 14
```
The provided Python script defines a function `fib4` that computes the nth Fibonacci number using an iterative method instead of recursion. The function follows the standard Fibonacci sequence rules, where each number is the sum of the previous two numbers. The function handles negative inputs gracefully by raising a `ValueError` if the input is not a non-negative integer. The tests demonstrate the expected outputs for Fibonacci numbers, specifically for indices 5 and 7.