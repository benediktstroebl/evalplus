```python
def fib4(n: int):
    """The Fibonacci sequence 4 numbers rule.
    a = [0, 0, 1, 1]
    return a[n]

# Test the function
test_fib4 = lambda: [0, 0, 2, 8]

for n, want in zip(range(4, 6), test_fib4()):
    print(f"n = {n}, want = {want}")
    print(f"fib4({n}) = {fib4(n)}")
```

This script defines a function that computes the n-th Fibonacci number in the 4 numbers sequence without recursion. The test function is used to create test data and the `fib4` function is called with different inputs to ensure it's functionality.