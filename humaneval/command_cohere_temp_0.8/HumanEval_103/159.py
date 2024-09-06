Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    binary_str = '-1'
    avg = (n + m) // 2

    if n <= m:
        avg = round(avg)
        binary_str = bin(avg)[2:]

        if len(binary_str) < 2:
            binary_str = '0' + binary_str
    return binary_str
```

The function directly computes the average of the two numbers and rounds it using the `round` function. The binary value is obtained by converting the rounded average to a binary string. If the binary string is too short, it is padded with a "0" prefix to ensure len(binary_str) == 2. Lastly, return `-1` if `n` is greater than `m`, following the spec. 

This solution employs basic Python functionalities and adheres to the problem's specified requirements.