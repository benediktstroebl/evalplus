```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    a, b = 0, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14)
```
The code defines a function fib4 that computes the n-th Fibonacci number in a non-recursive manner. It initializes theProcesses with the base cases for n=0,1, and 2, and then uses a loop to calculate Fibonacci numbers from the third element up to the n-th element. The code is self-contained and efficient for computing Fibonacci numbers.