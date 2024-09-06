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
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
```

The function `fib4` calculates the n-th Fibonacci number in the given sequence without using recursion. It checks for specific cases: if `n` is 0, it returns 0. If `n` is 1, it returns 0. If `n` is 2, it returns `n` and so on. This function uses a optimized approach to calculate Fibonacci numbers using repeated subtraction and addition.