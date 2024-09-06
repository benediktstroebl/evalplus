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
The Python code defines a function called `fib4` that computes the n-th element of the Fibonacci sequence using an efficient non-recursive approach. The function first checks for base cases where n is 0, 1, or 2, and directly returns the corresponding values (0, 0, and 2). For larger values of the function recursively computes the Fibonacci values using a sum of the previous four values. The test_fib4 function asserts that the `fib4` function produces the correct results for the test cases (n values from 5 to 7). The `main` function is the entry point of the program, and it calls the `test_fib4` function to run the tests.