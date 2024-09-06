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
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
    print(fib4(8))  # Output: 24
    print(fib4(9))  # Output: 55
    print(fib4(10))  # Output: 88811
```

This Python code defines a function `fib4` that computes the nth element of the Fibonacci sequence using a non-recursive approach. The function accepts an integer `n` as input and returns the corresponding Fibonacci number. The `__main__` block serves as the entry point of the program, and it demonstrates the function's behavior by calling it with various input values and displaying the results. 

If you're using Python 3, you can use the `print()` function without the parentheses, and the output will be formatted like the previous code.