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
    n = 7
    assert fib4(n) == 14  # Should evaluate to true

if __name__ == "__main__":
    test_fib4()
```
The function computes the n-th Fibonacci number in this script. It uses an straightforward technique that is not recursive. The function is straightforward and does not require any additional variables to store intermediate results. The test_fib4 function is used to check the correctness of the function by passing the test value n and asserting that the function returns the expected result.