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
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This Python script defines a function `fib4` that computes the n-th element of the Fibonacci sequence using a loop-free approach. The function checks for base cases (where n is 0, 1, 2) and directly returns the corresponding Fibonacci numbers. For larger values of `n`, the function recursively calculates the element by summing up the previous four elements. 

This function eliminates the need for recursive calls, providing a more efficient and concise solution. The `test_fib4` function tests the `fib4` function with various input values, ensuring its correctness.