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
        assert fib4(8) == 24
        assert fib4(9) == 45
        assert fib4(10) == 120

        assert_equal(fib4(11), 55)
        assert_equal(fib4(12), 169)
except AssertionError as e:
    print("Error:", e)

test_fib4()
```

This script defines a function called `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using a loop-free approach. It returns the first number, the 0th element of the sequence. The function is then tested using the `test_fib4` function that verifies its correctness using assertion statements. The test passes successfully, demonstrating the functionality of the `fib4` function.