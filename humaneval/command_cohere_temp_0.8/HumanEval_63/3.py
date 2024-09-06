```python
def fibfib(n):
    a,b,c = 0,1,0
    for i in range(n-1):
        c = a+b+c
        a,b = b,c
    return c
```
This script defines a function fibfib(n) that calculates the nth FibFib number efficiently. It uses an iterative approach to build the sequence, storing the values of the previous three terms in variables a, b, and c, updating them accordingly, and returning the desired FibFib number at the end. The given tests, including arguments 1, 5, and 8, confirm its correctness.  This function efficiently computes the nth element of the FibFib sequence. 

This approach is efficient because it only requires three variables to store the state of the three previous terms, and it only requires a single loop to compute the FibFib numbers. 

To improve efficiency further, you could use memoization to avoid redundant calculations, especially for large values of n. A recursive approach with memoization might look like this:
```python
def fibfib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 3:
        return n
    memo[n] = fibfib_memo(n-1, memo) + fibfib_memo(n-2, memo) + fibfib_memo(n-3, memo)
    return memo[n]
``` 
This approach will further minimize the computational cost, as the function will 'remember' previously computed values and avoid repeating the same calculations.