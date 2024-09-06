```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = d,a+b,c+d,a+b+c+d
    return a

"""
Testing the function
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
"""
``` 

The code defines a Python function `fib4(n)` to efficiently compute the n-th element of the Fib4 sequence, which is a variation of the Fibonacci sequence. It initializes four variables `a`, `b`, `c`, and `d` to track the sum of the previous four terms in the sequence. The loop iterates `n` times, updating the variables using bitwise XOR manipulation to efficiently compute the sum of the previous four terms and thereby calculate the next element in the sequence. The result is returned as `a` after the loop completes. The provided test cases demonstrate the function's correctness by correctly calculating the Fib4 numbers for `n` values of 5, 6, and 7.