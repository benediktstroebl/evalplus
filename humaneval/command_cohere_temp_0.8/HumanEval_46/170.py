```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```
This script defines a function `fib4` which efficiently calculates the n-th element of the Fib4 sequence, as described in the problem statement. It initializes a list `fib4_list` with the initial terms of the sequence and then uses a loop to calculate subsequent terms by summing up the previous four elements in the sequence. 
The loop starts from index 5 to avoid rewriting the initial terms of the sequence (index 0 to 4) and calculates each subsequent term iteratively, updating the `fib4_list` accordingly. Finally, it returns the n-th term of the sequence when given a positive integer n.