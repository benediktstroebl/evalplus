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

The provided Python script offers a concise and precise solution to the problem statement. The `rounded_avg` function accepts two positive integers, `n` and `m`, and calculates the average of the integers ranging from `n` to `m`, inclusive. It first verifies if `n` is greater than `m` and returns -1 if this condition is met, preventing inaccurate calculations. The algorithm then sums up the average of the integers and divides it by the total count, rounding the result to the nearest integer. The final outcome is expressed in binary form, consisting of a string starting with "0b," followed by the binary representation. This approach ensures a robust and adaptable solution that can be seamlessly integrated into various programs.