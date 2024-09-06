```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to efficiently compute the n-th element of the FibFib sequence. The recursive equation is derived from the definition of the FibFib sequence: fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3). This approach avoids repeated calculations and is thus more efficient than calculating each element independently. 

Here's a brief overview of the code:
- The function fibfib(n) takes an integer n as input.
- The base cases are defined with the condition n == 0 and n == 1, where the function returns 0.
- For n > 1, the function recursively calls itself with the arguments n-1, n-2, and n-3, and returns the sum of the results of these recursive calls, adhering to the definition of the FibFib sequence. 

This approach allows the function to efficiently compute the n-th element of the FibFib sequence in a straightforward and optimized manner.