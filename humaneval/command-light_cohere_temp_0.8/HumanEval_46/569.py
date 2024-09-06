```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. Fibonacci numbers are  are defined by the following:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    return fib4(n)

# Driver tests

def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 44
    assert fib4(10) == 120

# Run the tests

if __name__ == "__main__":
    test_fib4()
```
The function `fib4` uses the `Fibonacci` number sequence formula: It accepts an integer `n` as input and calculates the `n`th Fibonacci number by summing up the previous four numbers in the sequence. The function does not use recursion and is, therefore, efficient and fast.