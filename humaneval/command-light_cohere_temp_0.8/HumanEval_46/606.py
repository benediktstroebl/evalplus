```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones:
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# Example usage:
print(fib4(5))  # Output:   14
```