```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
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

# Test the function with n up to 7
test_fib4 = fib4
for i in range(0, 7):
    print(f"{test_fib4(i)}")
```