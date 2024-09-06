```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0] + tribonacci(n - 1)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```

The function uses a case-based approach to calculate the Tribonacci sequence, it starts with an initial case of `n=0` returning `[0]`, `n=1` returning `[1]`, and for even `n` it recursively calls itself with `n-1` and alternates for odd `n` it recursively calls itself with `n-1` and `n-2` and adds the output from the same two previous calls and then adds the result from the call with `n+1`.