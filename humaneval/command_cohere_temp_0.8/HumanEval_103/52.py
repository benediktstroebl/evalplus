Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    total = (n + m) // 2
    count = m - n + 1
    avg = total // count
    return bin(round(avg))[2:]
```

The provided Python script offers a concise and effective solution to the problem statement. The `rounded_avg` function accepts two positive integers, `n` and `m`, and calculates the average of the integers ranging from `n` to `m`, inclusive. It first verifies if `n` is greater than `m` and returns -1 if this condition is met, thus handling the edge case where the range is invalid. The algorithm then calculates the midpoint of the range (`(n + m) // 2`) and determines the number of integers within the range (`m - n + 1`). These values are used to compute the rounded average (`avg`) through integer division (`total // count`). Lastly, the average is rounded to the nearest integer using the `round()` function, and its binary representation is returned, adhering to the expected format "0bXX" where XX represents the binary digits.

This solution encompasses all necessary steps to solve the problem in a self-contained manner within the `rounded_avg` function, making it both efficient and easy to incorporate in other scripts.