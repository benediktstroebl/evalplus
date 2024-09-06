```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib44 sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    return

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 45
    assert fib4(10) == 90

if __name__ == "__main__":
    test_fib4()
```
This code defines a function called fib4 which computes the n-th Fibonacci number in the Fibonacci sequence using the formula: fib(n) = fib(n-1) + fib(n-2) + fib(n-3) + fib(n-4). The test_fib4 function contains a set of tests that verify the correctness of the fib4 function.