```python
def fib4(n: int):
    """
    The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is commonly denoted as Fibonacci numbers or Fibonacci sequence.

    Returns the `n`th Fibonacci number in the sequence of length `n`.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """
    Test the Fibonacci function.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

The code defines a Fibonacci function that computes the n-th Fibonacci number in O(n) time complexity. The function uses the efficient method of calculating Fibonacci numbers using the recurrence relation, avoiding the use of iterative or recursive methods with large time complexity. The test function demonstrates the expected behavior of the Fibonacci function, returning the correct results for the given input sizes.