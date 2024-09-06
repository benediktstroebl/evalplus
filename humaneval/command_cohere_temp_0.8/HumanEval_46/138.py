```python
def fib4(n: int):
    if n < 0:
        raise ValueError(" fib4 does not support negative indices")
    if n < 4:
        return n
    fib4_arr = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib4_arr.append(fib4_arr[i-1] + fib4_arr[i-2] + fib4_arr[i-3] + fib4_arr[i-4])
    return fib4_arr[n]
```

This script defines the `fib4` function, which efficiently calculates the n-th element of the Fib4 sequence, as required by the problem statement. It initializes the Fib4 array and uses a loop to calculate the sequence elements for higher values of `n`. Then it returns the n-th element of the sequence. Also, the code includes a `validation` mechanism that checks if `n` is less than 4, it returns the value of `n`; otherwise, it returns the n-th value of the Fib4 sequence.  This ensures the function provides the correct results for tests like `fib4(5)`, `fib4(6)`, and `fib4(7)`.