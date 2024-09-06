```python
def fibfib(n):
    # Create an array to store fibfib values and initialize the first three values
    fibfib_array = [0, 0, 1]
    if n <= 3:
        return fibfib_array[n]
    
    # Use dynamic programming to compute fibfib values and return the n-th value
    for i in range(3, n + 1):
        fibfib_array[i] = fibfib_array[i - 1] + fibfib_array[i - 2] + fibfib_array[i - 3]
    
    return fibfib_array[n]
```

This script's `fibfib` function uses dynamic programming to efficiently compute the n-th element of the FibFib sequence, as per the problem statement. The initial three values are initialized and then populated accordingly. The `if` statement checks if `n` is within the range of the already computed values; if so, it directly returns the value. If not, it uses the recurrence relation to compute the missing values and returns the n-th value of the sequence.