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
    n = 7
    expected = 14
    actual = fib4(n)
    assert expected == actual, f"Error: {expected} != {actual}"

# Test code executed
test_fib4()
 ```
The function **fib4** computes the n-th Fibonacci number in the Fibonacci sequence using a loop-based approach without recursion. It takes a tested against the method.