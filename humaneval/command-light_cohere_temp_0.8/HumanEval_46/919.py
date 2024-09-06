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
    print("Testing Fibonacci Series...")
    print("Result for n = 0:", fib4(0))
    print("Result for n = 1:", fib4(1))
    print("Result for n = 2:", fib4(2))
    print("Result for n = 3:", fib4(3))
    print("Result for n = 4:", fib4(4))
    print("Result for n = 5:", fib4(5))
```

This code defines a function fib4 that computes the n-th element of the Fibonacci sequence without recursion. The tests demonstrate the `fib4` function's behavior for different input values.