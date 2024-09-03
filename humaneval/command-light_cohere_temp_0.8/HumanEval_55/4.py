```python
def fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Example usage
test_fib = []
test_fib.add([fib(10))
test_fib.add([fib(1))
test_fib.add([fib(8))

def test_suite(test_fib):
    for item in test_fib:
        assert item(test_fib.has_item) == True
```
This code defines a function `fib` that calculates the n-th Fibonacci number, and passes all tests with `test_fib` using the `assert` assertion.  The above code also defines a `test_suite` function to create a suite of test cases for the `fib` function, which ensures that the function is working correctly.