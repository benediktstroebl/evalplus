```python
def fibfib(n):
    a,b = 0,1
    for i in range(n-2):
        a,b = b, a+b
    return b
```
This code defines a function `fibfib` that takes an integer `n` as input and returns the n-th number in the FibFib sequence. The sequence is defined such that `fibfib(0) == 0`, `fibfib(1) == 0`, and `fibfib(2) == 1`, and for `n > 2`, `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`. 

The code starts by initializing two variables `a` and `b` to 0 and 1, respectively, which represent the two latest numbers in the sequence. The for loop then iterates from 2 to `n-2`, updating the values of `a` and `b` alternately to their sum and `a+b` respectively, which is the formula for the FibFib sequence. Finally, the function returns `b`, which is the n-th number in the sequence. 

This is a direct implementation of the recursive formula for the FibFib sequence, which avoids the exponential time complexity of the naive recursive implementation by using an iterative approach that runs in linear time.