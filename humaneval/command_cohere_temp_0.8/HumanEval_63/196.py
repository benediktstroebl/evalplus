```python
def fibfib(n: int):
    prev1, prev2, fibfib_number = 0, 0, 0
    while n > 0:
        fibfib_number = prev1 + prev2 + fibfib_number
        prev2, prev1 = prev1, fibfib_number
        n -= 1
    return fibfib_number
```

This approach uses a similar logic to Fibonacci but with 3 variables kept in mind: `prev1`, `prev2`, and `fibfib_number`. This is a recursive approach and the time complexity is similar to the standard Fibonacci sequence, where each element can be computed in O(1) but the sequence itself takes O(2^n) time to complete. 

To efficiently compute the n-th element of the FibFib sequence, you could use dynamic programming with memoization. However, without further context or constraints, we cannot provide an optimized version. Let us know if you'd like to explore further and provide more details!