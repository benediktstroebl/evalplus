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
    try:
        assert fib4(5) == 4
        assert fib4(6) == 8
        assert fib4(7) == 14

        print("Success!")

test_fib4()
```
The above Python script defines a function called `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using a loop-free approach. The function checks the general cases for the base cases: `n==0` returns 0, `n==1` returns 0, `n==2` returns 2, and `n==3` returns 0. For `n` else cases, the function recursively calls itself with the arguments `(n-1)`, `(n-2)`, `(n-3)`, and `(n-4)` until it reaches the base cases. The function then adds the numbers together and returns the sum. The `test_fib4` function is used to test the `fib4` function by calling it with the value `5` and asserting that the result is `4`. Finally, the `test_fib4` function is called to run the tests.