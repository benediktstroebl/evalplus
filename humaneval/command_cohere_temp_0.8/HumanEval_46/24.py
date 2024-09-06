```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```

This script defines the `fib4` function, which efficiently calculates the n-th element of the Fib4 sequence, as described in the prompt. It initializes a list `fib4_list` with the initial terms of the sequence and then uses a loop to calculate subsequent terms by summing the four previous terms in the sequence. Finally, it returns the n-th term of the sequence when given as input. 

This approach is iterative and avoids the potential stack-related limitations associated with recursive solutions, making it efficient for calculating larger values of `n`. 

This code can be copied and pasted into a Python environment or script to test and use directly.