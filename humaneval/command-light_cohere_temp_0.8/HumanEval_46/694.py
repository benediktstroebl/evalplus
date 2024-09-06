```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n < 2:
        return 2
    elif n <= 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Unit tests
def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

 ```
This code defines the `fib4` function, which computes the n-th Fibonacci number in the sequence without using recursion. The function uses a specific conditions to determine which Fibonacci number to return, based on the value of `n`.