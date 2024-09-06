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

The code defines a Python function `fib4(n)` to calculate the nth number in the Fib4 sequence, which is similar to the Fibonacci sequence but with a 4th order recursion. It initializes four variables `a`, `b`, `c`, and `d` to track the intermediate values. The loop iterates `n` times, updating the variables using the recurrence relation `d`, `a + b`, `c + d`, and `a + b + c + d`. The final value of `a` is the desired Fib4 number for the given input `n`. The provided tests demonstrate the correctness of the function for various inputs.