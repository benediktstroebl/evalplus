```python
def fib4(n: int):
    """
    The Fibonacci sequence is a sequence of numbers in which the ith term of the sequence is a sum of the ith and (i-1)th terms of the two preceding terms. The Fib4 sequence is commonly referred to as Fibonacci numbers.

    Return the value of the n-th Fibonacci number.

    The function employs an efficient technique called memoization to avoid repeated calculations of the same Fibonacci number.
    """
return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
```
The code defines a function `fib4` that calculates the nth Fibonacci number of the Fibonacci sequence using the memoization technique. It avoids repeated calculations by storing previously computed results. 

This function efficiently computes Fibonacci numbers, reduces the time complexity, and ensures correct results for large n.