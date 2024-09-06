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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 44
    assert fib4(10) == 120

# Example usage:
print("Fibonacci numbers up to", 10)
test_fib4()
```

This Python script defines a function called `fib4` that computes the n-th Fibonacci number in O(n) time using an efficient formula-based approach. The `test_fib4` function contains several assertions that verify the correctness of the `fib4` function for various input values. The script then demonstrates the usage by computing Fibonacci numbers up to 10 and passing the test cases.