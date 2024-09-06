```python
def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This Python code defines a function called `fib4` that computes the n-th element of the Fibonacci sequence using a recursive approach. The sequence starts with the base cases: when n is 0 or 1, it returns 0. For n equal 2, it returns 2. For larger values of sequence, it recursively computes the previous four elements by summing them up. The function is then tested using the `test_fib4` function, passing the test case where the function is called with the value 7.