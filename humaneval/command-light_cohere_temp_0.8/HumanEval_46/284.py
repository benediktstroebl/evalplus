```python
def fib4(n: int):
    if n <= 0:
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
    print("Fibonacci sequence starting from number 0:")
    print(fib4(0))
    print(fib4(1))
    print(fib4(2))
    print(fib4(3))
    print(fib4(4))
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
```