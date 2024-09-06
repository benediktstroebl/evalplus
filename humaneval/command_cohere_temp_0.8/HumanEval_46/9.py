```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```

This script defines the `fib4` function, which efficiently calculates the n-th element of the Fib4 sequence, as required by the problem statement. It initializes a list `fib4_list` with the initial values of the sequence and then iteratively computes subsequent elements using a loop (not recursion). The loop runs from 5 to `n` (the desired index to calculate), and at each iteration, it updates `fib4_list[i]` with the sum of the previous four elements. Finally, it returns `fib4_list[n]`, which is the n-th element of the Fib4 sequence.