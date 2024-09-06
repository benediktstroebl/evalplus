```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This function uses a recursive approach to calculate the Fibonacci sequence, which is an efficient way to compute the sequence for smaller values of `n`. However, due to its exponential time complexity, it is not suitable for larger values of `n`. 
If you're interested in computing the Fibonacci sequence for larger values, you might want to consider using dynamic programming approaches or iterative approaches, which are more efficient. For example, you can use a bottom-up recursive approach, also known as dynamic programming, to efficiently compute the Fibonacci sequence. Here's a version of the code that employs this method:
```python
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```
This bottom-up recursive approach is more efficient than the original recursive implementation for larger values of n due to the elimination of unnecessary recursive calls. It still has a time complexity of O(n) but avoids the exponential blow-up of the traditional recursive approach.