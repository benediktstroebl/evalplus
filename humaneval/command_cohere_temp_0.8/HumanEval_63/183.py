```python
def fibfib(n):
    # initialize the last three values of the sequence
    fibfib.sequence = [0, 0, 1]
    # initialize the idx to 3 since we only have the last 3 values stored
    fibfib.idx = 3
    # iterate until we reach the desired index 'n'
    while fibfib.idx < n:
        # update the next value in the sequence as the sum of the last 3 values
        fibfib.sequence[-1] = fibfib.sequence[-2] + fibfib.sequence[-3] + fibfib.sequence[-4]
        # increment idx
        fibfib.idx += 1
    # return the nth value in the sequence
    return fibfib.sequence[n]
```

The code uses a Python class with a class variable to store and efficiently compute the FibFib values. The `fibfib()` function is a factory method that computes the n-th value efficiently by building up the sequence incrementally. It achieves this without storing every value in memory by updating the sequence and keeping track of the index (`fibfib.idx`) in a coordinated manner.