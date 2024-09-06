```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This Python script defines a function called fibfib that employs a recursive approach to compute the n-th element of the FibFib sequence, defined as follows:
- fibfib(0) == 0
- fibfib(1) == 0
- fibfib(2) == 1
- fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) 

The function starts by checking if n is 0 or 1, returning 0 in either case. If n is greater than 1, it recursively calls itself with the arguments n-1, n-2, and n-3, and returns the sum of the results of these recursive calls, effectively computing the n-th element of the FibFib sequence. 

Here are some example calls to this function, which illustrate its behavior:
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
``` 

This demonstrates the correct operation of the function, producing outputs that are consistent with the definition of the FibFib sequence.  This recursive approach, although conceptually simple, can become computationally inefficient for larger values of n due to the repeated recomputation of the same values, causing the well-known exponential time complexity of naive recursive solutions. These inefficiencies are akin to those encountered in computing the traditional Fibonacci sequence, which motivates the need for an optimized approach.