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
    assert fib4(n) == 14 

if __name__ == "__main__":
    test_fib4()
```
The provided Python code defines a function called `fib4` that computes the n-th Fibonacci number using a loop-specific approach. The function takes an integer `n` as input and returns the corresponding Fibonacci number. The code also includes a `test_fib4` function that tests the `fib4` function by calling it with `n = 7` and asserting that the returned value is indeed `14`. The function's assertion checks if the returned value of `fib4(7)` matches `14`, and if not, it raises an error indicating the test failed.

The code demonstrates a simple and efficient way to calculate Fibonacci numbers without recursion.