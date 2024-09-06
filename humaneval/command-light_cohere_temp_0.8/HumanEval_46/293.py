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
This script defines a function `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using the formula- `fib4(n) = fib4(n-1) + fib4(n-2) + ... + fib4(n-3)`. The `test_fib4` function tests the `fib4` function with different values of `n` to ensure that the function behaves correctly. The `main` function is the entry point of the script, which calls `test_fib4` to run the tests.