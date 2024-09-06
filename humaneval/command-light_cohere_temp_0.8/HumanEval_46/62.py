```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence is not defined for all integers n. The function is designed to efficiently compute the n-th element of the Fibonacci sequence using a mathematical formula.

    if n < 0 or calculating 0 and 1, they return 0 and 1 respectively.
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

test_fib4 = []

test_fib4.append(range(4))
test_fib4.append([fib4(x) for x in range(4)])

test_fib4
```

This Python script defines a function called fib4 that computes the n-th element of the Fibonacci sequence. The function uses a mathematical formula to calculate the sequence, and it handles the base cases for n equal to 0, 1, and 2. The function is then tested with test_fib4, which contains a series of tests for the fib4 function, ranging from 0 to 4.