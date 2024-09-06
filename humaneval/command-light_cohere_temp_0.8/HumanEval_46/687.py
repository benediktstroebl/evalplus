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
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    n = 7
    assert fib4(n) == 14  # Should be true

if __name__ == "__main__":
    test_fib4()
```
The function is a recursive implementation of the Fibonacci sequence, where each number is the sum of the previous four numbers. The test_fib4 function will call the fib4 function with n = 7 and will verify that the result is correct, which is indeed 14.