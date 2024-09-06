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
```

The code defines a function called `fib4` which computes the n-th element of the Fibonacci sequence using the recursive approach. The function takes an integer `n` as input and returns the corresponding Fibonacci number. 

The test_fib4 function contains assertions that verify the correctness of the `fib4` function by testing it with different values of `n`.