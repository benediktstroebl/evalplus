Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0 or diff % 2 == 0:
        return binary
    else:
        return -1
```
This function calculates the average of the integers between `n` and `m`, inclusive. If the difference between `n` and `m` is odd or if it is negative, it returns `-1` since the average is not reachable as a binary number. Otherwise, it calculates the average, rounds it to the nearest integer and returns it in binary format.