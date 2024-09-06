```python
def fibfib(n):
    # Handle special cases
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Use dynamic programming to avoid redundant computations
    fib = [0, 0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
    
    return fib[n]

# Unit tests
tests = [
    (0, 0),
    (1, 0),
    (2, 1),
    (5, 4),
    (8, 24),
]

for n, expected in tests:
    assert fibfib(n) == expected
```

The `fibfib` function uses dynamic programming to efficiently compute the n-th element of the FibFib sequence. It handles the base cases (`n == 0`, `n == 1`, and `n == 2`) directly, and then iterates from 3 to n, building up the FibFib sequence element by element using a list (`fib`) to store the computed values. This avoids redundant computations and significantly improves efficiency compared to a recursive approach that recalculates previous elements repeatedly. The unit tests demonstrate the correctness of the function for various inputs.