```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each successive number is a fraction of the sum of the two preceding ones."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Test
print(fib4(5))
```