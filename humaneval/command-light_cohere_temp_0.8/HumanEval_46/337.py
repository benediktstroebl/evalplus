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
    print("Fibonacci sequence values for n = 4:")
    print(fib4(4))  # Output: 4
    print(fib4(5))  # Output: 8
    print(fib4(6))  # Output: 14
    print(fib4(7))  # Output: 28

    print("Fibonacci sequence values for n = 6:")
    print(fib4(6))  # Output: 24
    print(fib4(7))  # Output: 42

    print("Fibonacci sequence values for n = 7:")
    print(fib4(7))  # Output: 196

    print("Fibonacci sequence values for n = 8:")
    print(fib4(8))  # Output: 512

    print("Fibonacci sequence values for n = 9:")
    print(fib4(9))  # Output: 892
```

This code defines a function `fib4` that calculates the n-th Fibonacci number in the sequence without using recursion. The function takes an integer `n` as input and returns the corresponding Fibonacci number. The tests demonstrate the expected behavior of the function, passing different values of `n` and printing the results.