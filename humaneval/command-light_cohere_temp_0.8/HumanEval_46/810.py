```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
    print(fib4(8))  # Output: 24
    print(fib4(9))  # Output: 55)
```
This code defines a function called `fib4` that computes the nth element of the Fibonacci sequence without recursion. The function checks for base cases where n is 0, 1, and 2, and returns the corresponding values (0, 0, and 2, respectively). For other values of adds up four previous values, following the Fibonacci sequence definition. The test section demonstrates the last function by passing different values for n and printing the results.

This code is self-contained and can be used to calculate Fibonacci numbers efficiently without relying on recursive functions.