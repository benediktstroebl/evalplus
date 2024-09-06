```python
def fibfib(n):
    a,b,c = 0,1,1
    for _ in range(3,n+1):
        a,b,c = c,a+b,b+c
    return a
```
This script defines a function `fibfib(n)` that uses a loop to efficiently calculate the nth value of the FibFib sequence, and returns the value of a using the given formula. 
This formula is more efficient than the original Fibonacci formula and can compute the th value in only 3 additions and 2 variables. The efficiency of this formula can be further improved to O(n) using dynamic programming but that would require using previous values and violating the self-containment constraint.  This solution efficiently computes the FibFib value in O(n) time complexity with only 3 variables and 3 additions.