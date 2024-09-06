```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursive calls to the previous three terms in the sequence, with the base cases for 0 and 1, as defined in the problem. And since this is a recursive algorithm, it is inherently inefficient for larger values of `n` due to the repeated computation of the same subproblems.

However, if you're interested in a more efficient solution, I would need to make some assumptions about efficiency and use a loop-based approach to solve this problem. Let me know if that sounds suitable, and we can modify the solution accordingly.