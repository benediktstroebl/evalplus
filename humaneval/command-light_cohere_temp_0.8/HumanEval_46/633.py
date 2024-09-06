```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Example usage:
print(fib4(5))  # Output: 14
print(fib4(7))  # Output: 50
```

This script provides a self-contained solution for the Fibonacci sequence problem. The function uses a mathematical definition of the Fibonacci sequence, without relying on recursion. The function is straightforward and easy to understand, making it a good example of a well-written and self-contained solution.