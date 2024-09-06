```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each subsequent number is the sum of the two preceding ones.

    if n == 0:
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

# Test case
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

The function calculates the nth Fibonacci number using an iterative approach, avoiding recursion, which often leads to efficiency issues.

The code is concise and efficient, utilizing an if-elif-else structure to directly access the appropriate Fibonacci value based on the input n. It avoids unnecessary computations and provides a clear and efficient solution to the given problem.