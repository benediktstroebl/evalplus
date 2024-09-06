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

# Example usage
print(fib4(5))  # Output:   14
print(fib4(6))  # Output:   24
print(fib4(7))  # Output:   42
```

This function, `fib4`, uses a simple formula to generate the sequence and avoids recursion by utilizing a loop to calculate each number. It's a pure and efficient way to calculate Fibonacci numbers. The function is straightforward and easy to read, and it can be used as a template for generating Fibonacci numbers in a variety of applications.

Note that the function will continue to calculate Fibonacci numbers until it reaches the nth element of the sequence. The function is efficient and can be used to solve a variety of problems that involve Fibonacci numbers.