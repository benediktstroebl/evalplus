```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function fibfib() that computes the n-th number in the FibFib sequence, which is similar to the Fibonacci sequence but defined as fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3). The function starts with basis cases for n=0, n=1, and returns 0 for them, and for any other n, it recursively computes fibfib(n) by summing the previous three sequence elements.