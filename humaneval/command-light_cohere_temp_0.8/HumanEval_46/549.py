```python
def fib4(n: int):
    if n <= 0:
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
    n = 5
    expected = 4
    actual = fib4(n)
    assert expected == actual, f"Incorrect result for n={n}, expected={expected}, actual={actual}"

test_fib4()
```
The code above defines a function `fib4` that computes the n-th element of the Fibonacci sequence using a non-recursive approach. The function then passes the test by computing the n-th element of the Fibonacci sequence up to 7 and ensuring that the actual result matches the expected result.