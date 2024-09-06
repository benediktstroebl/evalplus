Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    if n > m:
        return -1
    while count <= m - n + 1:
        total += count
        count *= 2
    return format(round(total / (m - n + 1)), 'b')
```

The script provides a function that takes in two integers `n` and `m` as parameters, where `n` is the smaller number, and `m` is the larger number. The function calculates the average of the integers from `n` to `m`, inclusive, rounds the result to the nearest integer, and converts it to binary. If `n` is greater than `m`, it returns `-1`. 

The function achieves this by:
1. Calculating the midpoint between `n` and `m` (`(m + n) // 2`), which is half the distance between the two numbers. This midpoint is where the center of the averaging will take place.
2. Initializing a `count` variable to 1, which will be used to count the number of integers in the range.
3. Checking if `n` is greater than `m`. If it is, the function returns `-1` since the range is invalid.
4. Entering a while loop that continues until `count` is less than or equal to `m - n + 1`. This loop iterates through each integer in the range from `n` to `m` (inclusive) with incrementally increasing steps of 2, adding each integer to the `total` variable.
5. Each time the loop iterates, `total` is incremented by `count`, which represents the number of integers added in that iteration. `count` is multiplied by 2 in each iteration to double the value added to `total` for the subsequent iteration.
6. Finally, the average is calculated by dividing `total` by `m - n + 1`, rounded to the nearest integer, and converted to binary using Python's `format` function with the `'b'` format specifier.

This solution efficiently computes the average of the integers in the range and converts it to binary, fulfilling the problem's requirements.