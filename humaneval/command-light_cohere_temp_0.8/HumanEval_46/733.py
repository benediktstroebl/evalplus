```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. Fibonacci numbers are characteristic is that they start from 0 and 1, and each subsequent number is the sum of the previous two.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Example usage
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
The function `fib4` calculates the n-th element of the Fibonacci sequence using a loop and the above recursive formula.  It is way is to compute Fibonacci numbers, this approach is more efficient than the traditional recursive method.