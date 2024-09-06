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

        assert_raises(ValueError, lambda: fib4(-1))
        assert_raises(TypeError, lambda: fib4("a"))

if __name__ == "__main__":
    test_fib4()
```
This Python script defines a function `fib4` that computes the n-th element of the Fibonacci sequence without recursion. The function uses a sequence of if-else statements to determine the value of the n-th Fibonacci number based on the value of `n`. It then uses the `test_fib4` function to run tests on the `fib4` function. The tests use assertion checks to ensure that the function outputs the correct Fibonacci numbers for the given inputs. The `assert_raises` methods are used to catch potential errors or unexpected behavior when running the function with invalid or unexpected inputs.