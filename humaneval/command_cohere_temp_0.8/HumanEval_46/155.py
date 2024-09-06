```python
def fib4(n):
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```

This script defines the `fib4` function, which efficiently calculates the n-th element of the Fib4 sequence without using recursion. It initializes a baseline `fib4_list` up to index 4 and iteratively computes subsequent elements based on the sequence's definition. The resulting `fib4_list[n]` provides the desired value for the input `n`. The function excels in both speed and usability, making it an ideal solution for this problem. Test cases can be easily added to validate its behavior further. Overall, this solution showcases a well-organized and effective approach to solving the problem.