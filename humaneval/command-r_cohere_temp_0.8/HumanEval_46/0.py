```python
def fib4_efficient(n):
    """Computes the n-th element of the fib4 sequence defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """
    if n <= 1:
        return 0
    if n == 2:
        return 2
    prev3, prev2, prev1, prev0 = 0, 0, 2, 0
    for i in range(3, n+1):
        curr = prev3 + prev2 + prev1 + prev0
        prev3, prev2, prev1, prev0 = prev2, prev1, prev0, curr
    return curr

# Test cases
assert fib4_efficient(5) == 4
assert fib4_efficient(6) == 8
assert fib4_efficient(7) == 14
```