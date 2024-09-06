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
    for i in range(0, 7):
        print(fib4(i), end=' ')
    print()
```
The code defines a function `fib4` that computes the n-th element of the Fibonacci sequence without recursion. The `__main__` block then calls this function 7 times, and the results are printed to the console.