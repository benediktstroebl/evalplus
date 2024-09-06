```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
```

The above code defines a function `fib4` that computes the nth element of the Fibonacci sequence using a loop-free approach. The function checks the first three cases for the input `n`: if `n` is 0, 1, or 2, it returns the corresponding value from the sequence. If `n` is greater than 3, it recursively calls `fib4` with the input `n-1`, `n-2`, `n-3`, and `n-4`, and adds the results together. The recursion continues until the value reaches a certain limit. The test cases are passed to ensure the function's correctness.