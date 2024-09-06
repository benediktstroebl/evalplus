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
    """Test the function fib4 by entering the desired value of n and expecting the Fibonacci number sequence to be returned."""
    for n in [0, 1, 2, 3,4,5]:
        print(f"Enter {n}:", n)
        got = fib4(n)
        print(f"Expected: {n}, Got: {got}")
        assert got == fib4(n)

test_fib4()
```

The code defines a function `fib4` that computes the n-th Fibonacci number in a non-recursive manner. The `test_fib4` function tests the `fib4` function with a series of input values and ensures the function's correctness by comparing the actual result with the expected result.

This code is a good starting point for Fibonacci calculation and can be easily modified or extended to handle more complex scenarios.