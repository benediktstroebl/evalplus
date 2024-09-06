```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = d,a+b,c+d,a+b+c+d
    return a
```

This script defines a function `fib4` which uses an iterative approach to calculate the nth Fib4 number without using recursion. It uses a 4-value state and updates these values iteratively. The output of this function is consistent with the definition of the Fib4 sequence provided in the problem statement.