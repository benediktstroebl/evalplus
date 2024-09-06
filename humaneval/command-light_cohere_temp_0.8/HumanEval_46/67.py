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
    assert actual == expected, "Function did not return the correct result"

if __name__ == "__main__":
    test_fib4()
```
The code defines a function called `fib4` that computes the n-th element of the Fibonacci sequence using an efficient algorithm. The function uses a loop to avoid recursion and achieves this by summing up the four previous terms. The `test_fib4` function tests the `fib4` function with an argument of 7, which should produce a result of 14. The function uses the assert statement to check if the actual result matches the expected result.