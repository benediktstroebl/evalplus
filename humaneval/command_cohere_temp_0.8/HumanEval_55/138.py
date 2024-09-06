```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `Fibonacci sequence` is a series of numbers in which each number (known as a Fibonacci number) is the sum of the two preceding ones. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

This problem asks us to write a function that will return the n-th Fibonacci number. It provides a simple outline and tests that the function works for the first 3 values of n it should:
- Return 1 for n=1.
- Return 2 for n=2.
- Return 3 for n=3.
- Return 55 for n=10.

Our Python code defines a function `fib(n)` that implements this recursive definition of the Fibonacci sequence. The base case checks if `n` is less than 2, in which case it returns `n` since the first two numbers in the sequence are 0 and 1. Otherwise, it recursively calls `fib(n-1)` and `fib(n-2)` to get the sum of the two previous Fibonacci numbers, which will be the n-th Fibonacci number we're looking for.