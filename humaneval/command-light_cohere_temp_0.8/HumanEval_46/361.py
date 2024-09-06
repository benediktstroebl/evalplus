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

This code defines a function called fib4 which calculates the n-th element of the Fibonacci sequence using the iterative approach. The function takes an input n and returns the nth Fibonacci number. The test cases at the main function demonstrate the functionality of the fib4 function by passing different values for n and printing the results.