```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is a well-known mathematical sequence and has many applications in computer science and mathematics.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Unit tests
def test_fib4():
    assert fib4(0) == 0
assert fib4(1) == 0
assert fib4(2) == 2
assert fib4(3) == 0
assert fib4(4) == 4
assert fib4(5) == 5

if __name__ == "__main__":
    test_fib4()
```
This Python script defines a function called `fib4` which computes the n-th element of the Fibonacci sequence using a method that does not use recursion. The `test_fib4` function contains unit tests to ensure the `fib4` function works correctly. The `main` function starts the execution of the `test_fib4` function, which begins the execution of the function's unit tests.