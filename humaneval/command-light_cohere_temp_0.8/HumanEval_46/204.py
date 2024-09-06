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
    test_fib4 = []
    test_fib4.append(fib4(5))
    test_fib4.append(fib4(6))
    test_fib4.append(fib4(7))
    for x in test_fib4:
        print(x, end=' ')
```