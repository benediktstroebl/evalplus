Here's a Python script with a self-contained function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    num_sum = (n + m) // 2
    rounded_sum = round(num_sum)
    return f"0b{bin(rounded_sum)[2:]}"
```

The provided Python script defines a function `rounded_avg(n, m)` that calculates the average of integers between `n` and `m`, inclusive. If `n` is greater than `m`, it returns -1. Otherwise, it computes the sum of integers between the two parameters, rounds it to the nearest integer, and converts the result to binary using the `bin` function. The script's approach ensures accuracy and utilizes built-in functions for efficient binary conversion.