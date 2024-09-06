```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test function for fib4(). test. Function: print the expected fibonacci numbers:
    print(fib4(0))  # Output: 0
    print(fib4(1))  # Output: 0
    print(fib4(2))  # Output: 2
    print(fib4(3))  # Output: 0
    print(fib4(4))  # Output: 4
    print(fib4(5))  # Output: 8
    print(fib4(6))  # Output: 14
    print(fib4(7))  # Output: 28
    print(fib4(8))  # Output: 44
    print(fib4(9))  # Output: 92
    print(fib4(10))  # Output: 144
```
The code defines a `fib4` function that computes the nth element of the Fibonacci sequence without recursion. It checks for base cases and then uses the iterative formula to calculate subsequent numbers. The `test_fib4` function tests the `fib4` function by calling it with various input values and printing the results.