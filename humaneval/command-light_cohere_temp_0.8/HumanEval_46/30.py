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
    n = 7
    expected = 14
    actual = fib4(n)
    assert actual == expected, f"Failed, expected {expected} but got {actual}"

test_fib4()
```
The code defines a Fibonacci sequence generator function, `fib4`, which uses a recursive approach without utilizing extra variables for memoization. It then contains a test function `test_fib4`, which generates a Fibonacci number sequence for the given input `n` and compares the actual result with the expected value, asserting if they match. 

This self-contained Python solution demonstrates the generation of Fibonacci numbers using recursion, along with a simple test to ensure its correctness.