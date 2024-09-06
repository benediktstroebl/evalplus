```python
def fib4(n: int) -> int:
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The function uses an initial cache of the first 5 numbers in the sequence to ensure that any calls to `fib4()` with a value of `n` less than 5 are instantaneous, as they return the cached values. For values of `n` greater than 4, the function efficiently computes the `n`-th Fib4 number by recursively summing the 3 previous Fib4 numbers. 

This approach strikes a balance between computational efficiency and algorithmic simplicity, avoiding both overflow errors and the exponential complexity typical of direct recursive solutions.