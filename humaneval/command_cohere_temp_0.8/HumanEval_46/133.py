```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```
This code defines a function `fib4` that efficiently calculates the n-th element of the Fib4 sequence, as described in the prompt, by using an iterative approach instead of recursion. It initializes a list `fib4_list` with the first five elements of the sequence and then iteratively computes subsequent elements by summing up the values from the previous four elements in the sequence. Finally, it returns the n-th element from the `fib4_list`.