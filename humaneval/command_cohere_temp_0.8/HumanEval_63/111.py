```python
def fibfib(n):
    a,b = 0,1
    for i in range(n-2):
        a,b = b, a+b
    return b
```
This script defines a function `fibfib` that takes an integer `n` as input and returns the n-th number in the FibFib sequence. The sequence is defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

The function efficiently computes the n-th element of the FibFib sequence by iteratively calculating the sum of the previous two elements in the sequence starting from n-2 until it reaches the base case of 0 and 1. Then, it returns the computed value of b, which is the n-th FibFib number.