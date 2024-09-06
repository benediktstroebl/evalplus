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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```
The provided Python script defines a function `fib4` that computes the n-th element of the Fibonacci sequence using a loop-free approach. The `test_fib4` function asserts that the function's output matches the expected result for specific input values. The `main` function starts the execution of the `test_fib4` function, which serves as the unit test of the `fib4` function.  The verifies that expected outputs against the actual results.