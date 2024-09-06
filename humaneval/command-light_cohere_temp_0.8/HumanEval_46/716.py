```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which the next number is the sum of the two preceding ones:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2)

test_fib4 = [
    "def test_fib4():
        assert fib4(5) == 4
        assert fib4(6) == 8
        assert fib4(7) == 14
        assert fib4(0) == 0
        assert fib4(1) == 0
        assert fib4(4) == 6
        assert fib4(3) == 8
        assert fib4(10) == 55
]
```
The code defines a function called fib4, which computes the n-th element of the Fibonacci sequence using the specified formula. The function follows the pattern of checking for base cases and then using a recursive approach for larger values of n. The test_fib4 function contains various assertions that validate the correctness of the fib4 function for different inputs. The code is self-contained and does not rely on external functions or modules.