```python
def tribonacci(n):
    result = [0, 1, 3]
    while len(result) < n + 1:
        num = 1 if result[-1] == 0 else 3 if result[-1] == 1 else result[-1] + result[-2] + result[-3]
        result.append(num)
    return result[:n+1]
```

The function `tribonacci` uses an initial seed of `[0, 1, 3]` to initialize the first three numbers of the Tribonacci sequence. It then enters a loop that iterates until the length of the result list is equal to `n + 1`. Within the loop, it determines the next number in the sequence by selecting among `0`, `1`, and `3` (corresponding to the last, second-to-last, and third-to-last values in the sequence) based on the value of the previous value (`result[-1]`), and alternatively calculating the next value as `result[-1] + result[-2] + result[-3]` if the previous value is neither `0` nor `1`. Finally, the function returns the relevant portion of the `result` list that contains the first `n + 1` numbers of the Tribonacci sequence.