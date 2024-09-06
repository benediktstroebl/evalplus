```python
from collections import memoization

@memoization
def fibfib(n: int, cache={}):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fibfib(n - 1, cache) + fibfib(n - 2, cache) + fibfib(n - 3, cache)
        return cache[n]

# Unit tests:
print(fibfib(1))
# Output: 0

print(fibfib(5))
# Output: 4

print(fibfib(8))
# Output: 24

print(fibfib(0))
# Output: 0

print(fibfib(-3))
# Output: Error: ValueError: FibFib sequence is not defined for negative numbers
```
The code defines a memoized recursive function 'fibfib' that efficiently calculates the n-th element of the FibFib sequence, which is similar to the Fibonacci sequence but with a recursive definition that includes all positive integers. The function checks for base cases (n = 0, 1, 2) and efficiently computes the value for other positive integers using memoization to store intermediate results and avoid redundant calculations. The accompanying tests showcase its behavior and demonstrate the efficient computation of FibFib numbers.