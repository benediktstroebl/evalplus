```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each successive number is achieved by adding the two preceding ones. The Fibonacci sequence begins with 0 and 1, and subsequent numbers are obtained by summing the last two numbers.
    return: 0
    if n == 0
    return 0
    return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Example usage:
print(fib4(5))
```