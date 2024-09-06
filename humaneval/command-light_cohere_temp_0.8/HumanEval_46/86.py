```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib44 sequence is defined as:
    fib4(0) = 0
    fib4(1) = 1
    fib4(2) = 1
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """

    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14

    print("Success!")

```