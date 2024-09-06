```python
def fib4(n: int):
    """
    The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.

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
    """Test the function
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
```
The provided code defines a Python function called fib4 that computes the n-th element of the Fibonacci sequence using a recursive approach without using a loop. The function takes an integer n as input and returns the corresponding Fibonacci number. 

The test_fib4 function includes several test cases that verify the correctness of the fib4 function. The function uses the assert statement to check if the returned value of the fib4 function matches the expected value for a given input value.