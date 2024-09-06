Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded_avg = round(avg)
    return f"0b{bin(rounded_avg)[2:]}"
```

The script provides the rounded average of the given numbers `n` and `m` and returns the binary representation of the rounded average if the smallest integer is greater than the largest integer, it returns `-1`. The `round` function is used to round the average to the nearest integer, and the `bin` function converts the rounded average to a binary string. 

The code assumes that the input is validated and that both 'n' and 'm' are integer values greater than 0. You can test this function by calling it with different sets of inputs to see the resulting binary-converted averages.  For example:
```python
rounded_avg(1, 5)
# Output: "0b11"

rounded_avg(7, 5)
# Output: -1

rounded_avg(10, 20)
# Output: "0b1111"

rounded_avg(20, 33)
# Output: "0b11010"
``` 

The script handles the specified conditions and provides the appropriate result for each test case.