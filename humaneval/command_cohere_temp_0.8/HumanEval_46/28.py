```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```

This script defines the `fib4` function, which efficiently calculates the n-th element of the Fib4 sequence, as required by the problem statement. It initializes the first 5 elements of the sequence and uses a loop to calculate subsequent elements based on the definition. The computed result is stored in the `fib4_list` and returned for the given input n. The solution is designed to avoid recursion, adhering to the requirement specified in the problem.