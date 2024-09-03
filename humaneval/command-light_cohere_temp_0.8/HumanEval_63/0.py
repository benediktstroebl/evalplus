Here's the function:
```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursion to compute the n-th element of the Fibonacci sequence. It follows the Fibonacci addition by summing the last three terms of the sequence to calculate the next one. The base cases are defined for n=0 and n=1, returning 0 and 1, respectively. Each subsequent recursive call computes the recursive step (n-2) of the sequence, adding the previous two terms and the third term together. The function then.