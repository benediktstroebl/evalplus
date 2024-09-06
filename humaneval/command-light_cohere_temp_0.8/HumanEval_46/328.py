```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
    """
    range(n + 1):
        yield [0, 1]
        yield from fib4(2)
```

This function generates an infinite sequence of numbers, starting with 0 and 1, by using a generator expression. The function then yields the multiple numbers from the sequence and uses a recursive call to the `fib4` function with decreasing values of `n`. 

This code is self-contained, as it does not require any external functions or modules to run.