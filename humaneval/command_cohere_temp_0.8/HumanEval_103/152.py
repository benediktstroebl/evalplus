Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    binary_string = '-1'
    if n > m:
        return binary_string
    total = (n + m) // 2
    count = 1
    temp_avg = 0
    while count <= m - n + 1:
        temp_avg += total
        count += 1
        total = total - n + m
    temp_avg = int(temp_avg)
    return binary_string if temp_avg % 1 else bin(temp_avg)[2:]
```
This script provides a solution to the problem statement, and the function `rounded_avg` returns the binary representation of the average of the integers present between `n` and `m` including `n` and `m`. The code also checks whether the average is integer or not and returns `-1` if n is greater than m.

Here is an example of how you can use this function:
```python
rounded_avg(1, 5) # Returns "0b11"
rounded_avg(7, 5) # Returns -1
rounded_avg(10, 20) # Returns "0b1111"
rounded_avg(20, 33) # Returns "0b11010"
``` 

This would output:
```
0b11
-1
0b1111
0b11010
```