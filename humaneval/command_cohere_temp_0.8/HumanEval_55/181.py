```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `Fibonacci sequence` is an integer sequence where the first two terms are 0 and 1. All other terms are obtained by adding the preceding two values. Though it cannot be defined by a simple closed formula, it still has several interesting properties. Your function implements the Fibonacci sequence by recursively adding the two previous terms if the index is greater than 1. This is a classic example of dynamic programming, as it saves recomputation of previously computed values. 

Here is a test script that can be used to validate this function:
```python
def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(10) == 55
    assert fib(20) == 6765
```

This test suite contains a variety of indices to test the function. 

You can execute these tests by pasting both code blocks in a Python interpreter, or by saving them in files and running them as scripts. 

I hope this solves your question and is suitable for passing these tests. Let me know if you have any other questions or need further assistance!