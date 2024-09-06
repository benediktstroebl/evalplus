```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```

This script defines the `fib4` function, which efficiently calculates the n-th element of the Fib4 sequence, as described in the prompt. It initializes a starter list `fib4_list` with the first few elements of the sequence and then uses a loop to calculate subsequent elements and append them to the list. Finally, it returns the n-th element from the list. The script is self-contained and does not rely on any external dependencies or recursive calls.

Here is an example of an iteration of the loop:
```python
fib4_list = [0, 0, 2, 0]
for i in range(5, n + 1):
    fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
```

In this iteration, `fib4_list` is initialized with the first four elements of the Fib4 sequence. The `for` loop iterates from 5 to `n + 1` (where `n` is the target index). For each iteration, the sum of the previous four elements is calculated and appended to `fib4_list`. This efficiently builds the list with the Fib4 sequence up to index `n`. 

Note that this solution uses a loop instead of recursion to achieve optimal performance and efficiently compute the Fib4 value for the given index `n`.