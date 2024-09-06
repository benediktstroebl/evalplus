```python
def fib4(n: int):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = d,a+b,c+d,a+b+c+d
    return a
```

This script defines a function `fib4` which uses an iterative approach to calculate the nth Fib4 number without using recursion. It uses a 4-tuple (a, b, c, d) to efficiently keep track of the state of the computation. The current state is updated in each iteration of the loop, and after all iterations, the a member of the tuple is the desired Fib4 number for the given input n. This approach avoids the exponential complexity of pure recursion and leads to a more efficient computation.