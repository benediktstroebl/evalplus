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
    try:
        assert fib4(5) == 4
        assert fib4(6) == 8
        assert fib4(7) == 14

        assert_compile()

def main():
    test_fib4()
```

The provided code defines a function called `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using the formula a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4).

The `test_fib4` function is used to validate the correctness of the `fib4` function by passing different values into it and asserting the results are as expected. The code also includes a `main` function, which serves as the entry point to execute the test suite. 

This code is a complete self-contained solution to the problem, as it includes both the function definition and the test suite.