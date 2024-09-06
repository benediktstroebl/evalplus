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
    """Test case 1:
    assert fib4(5) == 4

    """Test case 2:
    assert fib4(6) == 8

    """Test case 3:
    assert fib4(7) == 14

    """
test_fib4()

```
The function `fib4` calculates the n-th Fibonacci number in the Fibonacci sequence using the formula `nth-1 + n-2 + n-3 + n-4`. The test cases are defined to ensure that the function produces the correct results.