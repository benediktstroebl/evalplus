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
        return fib4(n-1) + fib4(n-2)

>>> fib4(0)  # Output: 0
>>> fib4(1)  # Output: 0
>>> fib4(2)  # Output: 2
>>> fib4(3)  # Output: 0
>>> fib4(4)  # Output: 4
>>> fib4(5)  # Output: 5
>>> fib4(6)  # Output: 8
>>> fib4(7)  # Output: 14
```
The function `fib4` calculates the nth element of the Fibonacci sequence using a loop that avoids recursion. It utilizes an if-else structure to handle different cases and returns the corresponding Fibonacci number.