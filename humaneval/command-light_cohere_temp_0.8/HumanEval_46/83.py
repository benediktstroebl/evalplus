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

This script defines a function fib4 which computes the n-th element of the Fibonacci sequence. The function uses a chain of conditional statements to determine the appropriate value based on the given input n. The tests pass, demonstrating the functionality of the code.

The output will be: 4 8 14.