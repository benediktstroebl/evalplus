```python
def fibfib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
```
This function uses a recursive approach to calculate the nth term of the FibFib sequence, adhering to the definition of the sequence. Essentially, it combines the last three terms of the sequence to generate the next term. The base cases of the function are also appropriately set to handle non-positive values, essentially returning 0 for such cases, as stipulated by the sequence definition.