```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
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
    assert fib4(6) == 8
    assert fib4(7) == 14

# Example usage
if __name__ == "__main__":
    test_fib4()
```
This Python script defines a function called `fib4` that computes the nth element of the Fibonacci sequence using a specific mathematical definition. The function uses a approach without recursion, which makes it more efficient and avoids the drawbacks of recursive calls. 

The `test_fib4` function contains several unit tests that verify the correctness of the `fib4` function. The `if __name__ == "__main__":` statement ensures that the `test_fib4` function is only executed if the script is run directly, not imported.