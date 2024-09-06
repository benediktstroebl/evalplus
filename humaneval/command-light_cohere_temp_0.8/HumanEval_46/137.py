```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which the next term is the sum of the two preceding terms. Fibonacci numbers are first defined by medieval mathematicians, and are a sequence of numbers that begins with 0 and 1, and each subsequent number is the sum of the previous two numbers. The Fibonacci sequence can a four numbers that, when concatenated, are shown in the sequence.
    ```
def test_fib4():
    """This function tests the correctness of the fib4 function."""
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```