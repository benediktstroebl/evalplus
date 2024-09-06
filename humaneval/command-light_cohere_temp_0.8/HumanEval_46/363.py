```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which the next number is the sum of the two preceding ones. The Fib4 sequence is similar to the Fibonacci sequence but is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """
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
    """Test the fib4 function using the following tests:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

This Python script defines the fib4 function, which computes the n-th element of the Fibonacci sequence using an efficient approach. It uses a both base cases and the summation of the previous four numbers to compute the nth Fibonacci number. The test_fib4 function contains several test cases to verify the correctness of the fib4 function.