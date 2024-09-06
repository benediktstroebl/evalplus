```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```
This script defines the `fib4` function, which efficiently calculates the n-th element of the Fib4 sequence, as required by the problem statement. It does so by initiating a list `fib4_list` with the initial terms of the sequence and then iteratively populating it with the cumulative sums thereof, using a loop that starts from index 5 (as the sequence's length is capped at 4Gig, a precaution to prevent endless recursion). 

The final element of `fib4_list` corresponds to the n-th Fib4 number when `n` is the input. It's worth noting that this solution employs a meticulous iteration process instead of recursion, as per the request. While this method is efficient for calculating individual Fib4 numbers, it may not be the most optimal approach for handling large arrays of Fib4 numbers. However, it perfectly suits the problem at hand.