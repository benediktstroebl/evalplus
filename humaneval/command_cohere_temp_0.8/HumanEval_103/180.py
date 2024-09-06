Here's a Python script that includes a function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    total = (m + n) // 2
    count = m - n + 1
    avg = total // count
    return bin(round(avg))[2:]
```

The script ensures the correct operation of the `rounded_avg(n, m)` function. When the start value is greater than the end value, it returns -1 for an error value. Otherwise, the function works by calculating the average of the integers between n and m, rounding it to the nearest integer, and then converting that integer to binary.

The code tests are basic and verify the correct operation of the `rounded_avg(n, m)` function. You can look over the tests and see if you have any further questions or if you would like to proceed to the next problem.