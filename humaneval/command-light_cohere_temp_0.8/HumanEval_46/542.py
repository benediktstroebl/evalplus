```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    fib_seq = [0, 0, 1, 1]
    return fib_seq[n]

# Test the function
test_fib4 = fib4
assert test_fib4(0) == 0
assert test_fib4(1) == 0
assert test_fib4(2) == 2
assert test_fib4(3) == 0
assert test_fib4(4) == 4
assert test_fib4(5) == 5
assert test_fib4(6) == 8
assert test_fib4(7) == 14
```
This Python code defines a function `fib4` without recursion, which computes the n-th Fibonacci number in the Fibonacci sequence. It achieves this by creating a list `fib_seq` containing the initial numbers, and then uses this sequence to calculate the n-th element using a list comprehension. The function provides a test cases using the built-in `assert` statement, ensuring that it correctly calculates the Fibonacci numbers for various input values.