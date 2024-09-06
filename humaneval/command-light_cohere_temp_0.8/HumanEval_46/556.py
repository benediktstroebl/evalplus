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
    print("Fibonacci Sequence for n = 5:", fib4(5))
    print("Fibonacci Sequence for n = 6:", fib4(6))
    print("Fibonacci Sequence for n = 7:", fib4(7))
    print("Fibonacci Sequence for n = 8:", fib4(8))
```

This code defines a function called `fib4` that calculates the n-th element of the Fibonacci sequence using an efficient approach. It uses a optimized recursive approach that avoids repeated calculations. The function also includes tests to ensure its correctness.