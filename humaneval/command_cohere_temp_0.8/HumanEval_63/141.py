```python
def fibfib(n):
    a,b,c = 0,0,1
    for _ in range(n-2):
        a,b,c = b,c, a+b+c
    return c
```
This script defines a function `fibfib(n)` that calculates the nth FibFib number efficiently. It uses an iterative approach to calculate the value, avoiding the exponential time complexity associated with recursive methods. The loop iterates through steps needed to calculate the FibFib numbers, updating the values of `a`, `b`, and `c` accordingly. The result is then returned as the value of the nth FibFib number.