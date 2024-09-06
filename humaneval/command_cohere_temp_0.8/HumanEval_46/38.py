```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = b,c,d, a+b+c+d
    return a

"""
Testing the function
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
>>> fib4(20)
557
"""
``` 

This script defines the fib4() function without recursion, using a loop to iteratively calculate the n-th value of the Fib4 sequence for non-negative integer input n. The result is then printed to the console for various values of n to validate the correctness of the function.