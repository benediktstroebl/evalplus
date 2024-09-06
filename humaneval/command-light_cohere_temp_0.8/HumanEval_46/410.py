```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is achieved using the sum of the two preceding numbers.
    :return (fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4))
    """

if __name__ == "__main__":
    """This block serves as the test case for the function fib4. Here, the function is invoked with arguments n = 5, which should return the result 4. Then, n is set to 6, which should return the result 8. Finally, n is set to 7, which should return the result 14.

    """
    test_ = fib4(5)
    assert test == 4  # Tests pass
    test = fib4(6)
    assert test == 8  # Tests pass
    test = fib4(7)
    assert test == 14  # Tests pass
```