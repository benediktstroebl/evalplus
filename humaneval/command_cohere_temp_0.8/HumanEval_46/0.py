```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```
This code defines a function `fib4` which efficiently calculates the n-th element of the Fib4 sequence, without using recursion. The sequence is initialized with the first 4 elements (as defined by the problem statement), and then the loop iterates from 5 to n, calculating each element of the sequence by summing up the previous 4 elements. Finally, the function returns the n-th element of the sequence.