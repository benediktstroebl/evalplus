```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a recursive function *fib* that returns the n-th Fibonacci number. The function checks if *n* is less than or equal to 1, returning *n* directly in such cases. If *n* is greater than 1, it calculates the Fibonacci number for *n* by summing the results of the previous two Fibonacci numbers and recursively calls *fib* with n-1 and n-2. This definition ensures that the Fibonacci sequence is correctly calculated, providing the desired result for the given input.  It passes the provided tests since it satisfies the given test cases: 1, 8, and 10. 
If the goal was to generate the Fibonacci series itself, the code would require additional manipulation to achieve that. However, the provided code perfectly satisfies the problem statement's requirement to return the n-th Fibonacci number.