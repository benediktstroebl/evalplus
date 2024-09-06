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
The function `fib4` takes an integer `n` as input and uses a series of conditional statements to determine the appropriate calculation path. It uses a recursive calls to compute the value of the n-th element in the Fibonacci sequence using a combination of addition and recursion. 

The `test_fib4` function tests the `fib4` function with various input values and asserts that the computed results are correct. The `main` function is the entry point of the script, it first calls `test_fib4` to run the tests and then calls `fib4` to compute Fibonacci values with various input values.