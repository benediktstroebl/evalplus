```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Function to test the fib4 function."""
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This Python script defines a function called fib4 that calculates the n-th element of the Fibonacci sequence using a specific method without recursion. The function follows the method to calculate Fibonacci numbers, which involves checking the base cases (n == 0, 1, 2) and then using a recursive approach to compute the remaining values. The test_fib4 function is also defined to test the correctness of the fib4 function by asserting that the calculated values match the expected results. 

This script provides a self-contained solution and test for the Fibonacci sequence problem using a recursive approach without using any external functions or modules.