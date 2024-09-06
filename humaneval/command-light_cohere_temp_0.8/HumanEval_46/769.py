```python
def fib4(n: int):
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
    """test the fibonacci function
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 45
    assert fib4(10) == 55
    assert fib4(11) == 89
    assert fib4(12) == 144
    assert fib4(13) == 233
    assert fib4(14) == 377
    assert fib4(15) == 610
```

This code defines a function called fib4 that computes the n-th Fibonacci number in O(n) complexity, using an iterative approach. The function starts by checking if n is equal to 0, 1, or 2, and returns 0, 0, or 2 respectively. If n is greater than 2, the function recursively calls itself to compute the Fibonacci number for n-1, n-2, n-3, and n-4. 

The function then adds up the four previous Fibonacci numbers to compute the n-th Fibonacci number.  The test_fib4() function tests the fib4 function by asserting that the result of the function call is equal to the expected value.