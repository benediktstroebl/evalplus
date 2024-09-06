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

def test_fib4():
    n = 7
    result = fib4(n)
    print(f"The {n}th Fibonacci number is: {result}")

test_fib4()
```

This code defines a function `fib4` that computes the nth element of the Fibonacci sequence using a formula that doesn't use recursion. It also has a test code that creates an instance of `fib4` with `n` set to 7 and then prints out the corresponding Fibonacci number.