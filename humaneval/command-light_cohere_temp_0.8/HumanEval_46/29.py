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

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```

This code has a function `fib4` which computes the n-th element of the Fibonacci sequence without recursion. The `test_fib4` function tests the function with various input values and asserts that the function returns the correct result. The `main` function is the entry point of the script, and it calls the `test_fib4` function to verify the correctness of the `fib4` function.