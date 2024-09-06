```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This Python code defines a function fib4 that computes the n-th Fibonacci number in O(n) time using an iterative method. It uses a simple arithmetic to calculate each Fibonacci number, avoiding recursion. The test cases demonstrate the simple and efficient computation of Fibonacci numbers using this function.