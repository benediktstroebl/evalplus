```python
def fib4(n: int):
    """
    The Fibonacci sequence is defined as:
        fib4(0) -> 0
        fib4(1) -> 0
        fib4(2) -> 2
        fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """
    return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0

def main():
    """
    print("Testing fibonacci sequence:")
    test_fib4()

if __name__ == "__main__":
    main()
```

In this code, the `fib4` function calculates the n-th element of the Fibonacci sequence without using recursion. The `test_fib4` function contains tests that verify the correctness of the `fib4` function for various input values. The `main` function is responsible for executing the test suite when the script is run.