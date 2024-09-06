```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It bases its logic on the fact that the Fibonacci sequence follows a recurrence relation, where each number is a sum of the two preceding ones. 

This function's iterative approach eliminates the need to store or calculate all Fibonacci numbers, making it more efficient than an outright recursive approach, especially for large values of `n`. It provides an optimized solution for the problem, avoiding the exponential time complexity associated with pure recursion or direct computation of all Fibonacci numbers.