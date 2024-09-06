```python
def fib4(n: int):
    if n <= 0:
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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 44
```
The above code defines a function called fib4, which computes the n-th value of the Fibonacci sequence. The function uses a series of if-else statements to determine the value of the n-th Fibonacci number based on the values of the previous four numbers. The test_fib4 function tests the fib4 function with various input values and asserts that the function returns the correct results.