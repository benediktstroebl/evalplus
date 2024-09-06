Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    if n > m:
        return -1
    while count <= m - n + 1:
        total += count
        count += 1
    rounded = round(total / (m - n + 1))
    if rounded == 0:
        return "0b0"
    binary = "{0:b}".format(rounded)
    return binary
```

The function takes two integers `n` and `m` as inputs and returns the binary representation of the average of the integers between `n` and `m` (including both). It initializes the `total` variable to store the sum of integers and the `count` variable to count the number of integers. If `n` is greater than `m`, it returns `-1`. The code uses while loop until the count reaches the difference between `m` and `n` to add the total and increment the count. It then rounds the total divided by the count and converts it to binary. If the rounded value is `0`, it returns "0b0". Otherwise, it returns the binary value.  This code aims to solve the problem statement efficiently and accurately.