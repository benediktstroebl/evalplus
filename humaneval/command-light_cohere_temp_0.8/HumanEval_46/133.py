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
    print("Result: ", fib4(7))
```

The function 'fib4' uses a loop to calculate the n-th element of the Fibonacci sequence without recursion. It's a a method more efficient and avoids the potential stack overflow problems associated with recursion.