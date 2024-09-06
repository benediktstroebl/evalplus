Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    binary_str = '-1'
    avg = (n + m) // 2

    if n <= m:
        avg = round(avg)
        binary_str = bin(avg)[2:]
        return binary_str
    else:
        return binary_str
```

The code tests the parameters against two conditions: being less than or greater than each other. Using the floor division operator (`//`) calculates the average of the two integers without rounding. Using the `round` function centers the average between the two numbers. The binary string is generated using the `bin` write method, providing a binary string representation of the rounded average. Finally, the code returns the binary string representation of the rounded average if the parameters are valid, and `-1` if the average is imbalanced. 

The code is self-contained and can be executed as a standalone Python script, and it also can be evaluated individually as a Markdown code block.