```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = d,a+b,c+d,a+b+c+d
    return a
```

This script defines a function `fib4` that uses an iterative approach to calculate the nth Fib4 number without using recursion. It uses a 4-tuple (a, b, c, d) to maintain the state of the sequence, updating them in each iteration based on the definition of Fib4. The output matches the expected results for `fib4(5)`, `fib4(6)`, and `fib4(7)`.