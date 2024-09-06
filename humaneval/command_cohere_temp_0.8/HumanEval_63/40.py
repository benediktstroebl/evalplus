```python
def fibfib(n: int):
    prev1, prev2, fibfib_num = 0, 0, 0
    while n > 0:
        fibfib_num = prev1 + prev2 + fibfib_num
        prev2, prev1 = prev1, fibfib_num
        n -= 1
    return fibfib_num
```
This function uses a proactive approach to calculate the nth term of the FibFib sequence by keeping track of the last 3 terms of the sequence, namely `prev1`, `prev2`, and `fibfib_num`, which map to the FibFib sequence values of n-1, n-2, and n respectively. It updates these values efficiently in a loop, avoiding the need to recursively calculate the entire sequence, and thereby improving time complexity. This allows the function to efficiently compute the n-th element of the fibfib number sequence.