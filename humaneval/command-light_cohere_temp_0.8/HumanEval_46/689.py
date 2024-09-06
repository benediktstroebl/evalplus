```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the first two are 0 and 1, and each subsequent number is the sum of the previous two.
    if n < 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return a

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```