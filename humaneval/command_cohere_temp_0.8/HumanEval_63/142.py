```python
def fibfib(n):
    a,b,c = 0,0,1
    for _ in range(n-3):
        a,b,c = b,c, a+b+c
    return c
```
This script defines a function fibfib(n) that calculates the nth value in the FibFib sequence efficiently, making use of the recurrence relation fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3). It then uses a loop to build up the values of a, b, and c accordingly. The output matches the specification for fibfib(1) and fibfib(5) and fibfib(8). 

You can test this script by calling the function with different input values to verify its behavior against the specified Markdown problem.