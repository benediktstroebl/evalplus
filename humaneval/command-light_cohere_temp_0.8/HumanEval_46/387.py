```python
def fib4(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    elif n == 4:
        return 1
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 45
    assert fib4(10) == 55
    assert fib4(11) == 89
    assert fib4(12) == 144

# Run the function test_fib4() to verify the correctness of the fib4 function
```