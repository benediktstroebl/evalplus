```python
def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```

The function fib4() uses an initial cache of the first 5 numbers in the sequence to ensure correctness for those particular inputs. It returns the cached values for n < 5. For n >= 5, it computes the n-th Fib4 number using the recursive formula fib4(n) = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4). The caching of the initial values ensures quick retrieval of the basis elements, thus optimizing the function's time complexity.