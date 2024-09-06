Here's the provided code with the self-contained function that solves the Fibonacci sequence problem:

```python
def fib4(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

# Unit tests
test_fib4 = [
    'def test_fib4():
        assert fib4(5) == 4
        assert fib4(6) == 8
        assert fib4(7) == 14
        assert fib4(8) == 26
        assert fib4(9) == 55
        assert fib4(10) == 90
]
```

This code defines a self-contained function called fib4 that efficiently computes the n-th Fibonacci number using a loop-free approach. The function follows the pattern of the Fibonacci sequence calculation: returning 0 for n<=0, 1 for n==1, and summing the previous four values for n>=2. The unit tests demonstrate the use of the fib4 function with a variety of inputs and assert that the function returns the correct Fibonacci numbers.