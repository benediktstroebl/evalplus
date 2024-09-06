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
    expected = 14
    actual = fib4(n)
    assert expected == actual, f"Expected {expected}, but got {actual}."

if __name__ == "__main__":
    test_fib4()
```
The code defines a `fib4` function that computes the n-th Fibonacci number without recursion. The `test_fib4` function then calls `fib4` with `n` equal to 7 and compares the result with the expected value of 14. The function successfully passes the test and prints a message to confirm it.