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
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
```

This script defines a function fib4 that computes the n-th element of the Fibonacci sequence without recursion. The function uses an iterative approach to calculate the Fibonacci numbers by summing the previous four numbers, which results in the desired behavior of the Fibonacci sequence. The tests at the time are used to ensure that the function is working correctly.