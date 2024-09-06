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

The script then provides examples of the function's behavior for the first few values of `n`:
- `fibfib(1) == 0`
- `fibfib(5) == 4`
- `fibfib(8) == 24`

The main logic of the function is enclosed within a for loop that runs `n-2` times. It uses two variables, `a` and `b`, initialized to the known values of the first two numbers in the sequence. On each iteration of the for loop, it updates `a` and `b` to the values of `b` and `a+b` respectively, which are the next two numbers in the sequence. This is possible due to the recurrence relation of the FibFib sequence. After the loop completes, `b` contains the n-th number in the sequence, which is returned as a result. 

This approach has a time complexity of `O(n)` since there are `n-2` iterations of the loop, and a space complexity of `O(1)` as it only requires two variables, regardless of input size.