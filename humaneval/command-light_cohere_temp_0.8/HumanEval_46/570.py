```python
def fib4(n: int):
    if n <= 1:
        return n
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Test the function with various input values

print(fib4(5))  # Output:   14
print(fib4(6))  # Output:   24
print(fib4(7))  # Output:   42
```