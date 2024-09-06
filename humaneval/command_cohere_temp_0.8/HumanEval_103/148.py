Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    total = (m + n) // 2
    count = m - n + 1
    if count == 0:
        return '-1'
    rounded_total = round(total)
    binary_representation = bin(rounded_total)[2:]
    return binary_representation if count > 0 else '-1'
```

#### Test Cases
```python
rounded_avg(1, 5)  # Should return "0b11"
rounded_avg(7, 5)  # Should return -1
rounded_avg(10, 20)  # Should return "0b1111"
rounded_avg(20, 33)  # Should return "0b11010"
``` 

This code defines a function called `rounded_avg` that takes two integers `n` and `m` as input. It calculates the average of the integers between `n` and `m`, inclusive. If `n` is greater than `m`, it returns `-1`. The average is then rounded to the nearest integer, and its binary representation is returned. If the average is zero (due to a count of zero), it returns `-1` to indicate an empty range.