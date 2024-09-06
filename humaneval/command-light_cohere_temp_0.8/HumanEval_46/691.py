```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each subsequent term is the sum of the previous two terms. Fibonacci(sequence) is the sequence defined as follows:
        fib4(0) -> 0
        fib4(1) -> 0
        fib4(2) -> 2
        fib4(3) -> 0
        fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    :param n: int
        :return: int
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

def test_fib4(n):
    """test
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    """test
    test_fib4(4)
    print('All tests passed!')

```
This script defines a Fib4 function that computes the nth Fibonacci number in the sequence using the formula:  `F(n) = F(n-1) + F(n-2) + F(n-3) + F(n-4)`. 

The `test_fib4` function tests the `fib4` function with different input values and verifies that the output matches the expected results. The `main` function orchestrates the test and output a success message.