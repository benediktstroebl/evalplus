Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    total = (m + n) // 2
    count = m - n + 1
    answer = bin(round(total / count))[2:]
    if n > m:
        return -1
    else:
        return answer
```
The function `rounded_avg` calculates the average of the integers from `n` through `m`, rounds it to the nearest integer, and then converts it to binary. If `n` is greater than `m`, it returns -1. Feel free to test this function with the given example and any other test cases you'd like!