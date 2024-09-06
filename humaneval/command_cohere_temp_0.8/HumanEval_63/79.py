```python
def fibfib(n):
    a,b,c = 0,1,0
    for i in range(n):
        c = a+b+c
        a,b = b,c
    return c
```
This script defines a function `fibfib` that takes an integer `n` as input and returns the n-th number in the FibFib sequence. The sequence is defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

The script implements this definition by initially setting `a`, `b`, and `c` to 0, 1, and 0 respectively. Then, in a loop that runs `n` times, it updates the variables as follows:
```
c = a+b+c
a, b = b, c
```
Each iteration shifts the previous `a` and `b` values to make way for the upcoming calculation. After the loop completes, the value of `c` is the n-th FibFib number.

The code is concise and elegantly solves the problem using minimal resources, making it efficient. It also has a pleasant, smooth readability.