```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

>>> fib4(5)
# Output: 4

>>> fib4(6)
# Output: 8

>>> fib4(7)
# Output: 14

>>> fib4(8)
# Output: 24

>>> fib4(9)
# Output: 44

>>> fib4(10)
# Output: 64

# Test suite using doctest
import doctest
doctest_run_tests()
```

This code defines a function called `fib4` that computes the n-th element of the Fibonacci sequence without recursion. The function initializes a sequence with the first two elements (0 and 1) and then iterates through the sequence starting from the third element up, adding the last two elements to compute the next value. The test suite uses the `doctest` to run the `fib4` function with various input values and checks the results against the expected outputs.