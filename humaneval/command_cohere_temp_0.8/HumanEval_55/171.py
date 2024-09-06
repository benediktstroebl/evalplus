```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a recursive function `fib` that calculates the n-th Fibonacci number. It checks if `n` is less than 2, returning `n` if so. If not, it returns the sum of the previous two Fibonacci numbers, calculated through recursive calls with `n - 1` and `n - 2`. This mirrors the classic definition of Fibonacci numbers, where each number is the sum of the two preceding ones. 

**NOTE:** The script's efficiency is linear since each Fibonacci number is computed twice, potentially leading to sizable execution times for higher `n`. This flaw could be improved with memoization or tail recursion, which optimize such recursive processes.