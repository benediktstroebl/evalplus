```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the first two are 0 and 1, and each subsequent number is the sum of the preceding two. The Fib4 sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """
    if n <= 0:
        return "Please enter a positive integer"
    return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Example usage
print(fib4(7))
```