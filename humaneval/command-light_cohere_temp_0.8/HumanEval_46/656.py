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
The code defines a Fibonacci sequence function `fib4` that computes the n-th element of the sequence using the recursive formula: `fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`. The function then includes a series of tests to ensure the correctness of the function.

The `main` function serves as the entry point of the script. It calls the function `test_fib4` to run the tests and demonstrate the function.