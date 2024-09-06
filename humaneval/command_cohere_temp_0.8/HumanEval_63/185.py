```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function that computes the n-th number in the FibFib sequence. It starts by checking for base cases: if n is 0 or 1, it returns 0. Otherwise, it recursively calls the function with n-1, n-2, and n-3, and adds the results to compute the n-th FibFib number. This algorithm is efficient for calculating individual FibFib numbers, but it is not efficient for calculating FibFib(n) for large n as it has an exponential time complexity similar to the classic Fibonacci sequence. 
It would be more efficient to generate the sequence iteratively only once and then perform calculations on the sequence as needed, rather than recomputing all the way to n every time. A common approach for this is to use memoization to store previously computed values and avoid redundant calculations. 
Here is a link to a Python version on GitHub that uses memoization: 
https://github.com/maziarraissa/fibfib-sequence/blob/main/fibfib.py