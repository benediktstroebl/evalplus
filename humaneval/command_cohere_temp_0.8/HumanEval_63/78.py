```python
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This Python script defines the function `fibfib` that employs recursive formulation to compute the n-th element of the FibFib sequence, as described in the problem statement. It provides an intuitive way to understand and solve the problem, making it a concise and clear solution.