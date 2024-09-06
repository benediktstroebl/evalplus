Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0 or diff % 2 == 0:
        return binary
    else:
        return -1
```
This function takes two integers `n` and `m` as arguments, and returns the binary representation of the average of the integers between them if `m` is less than or equal to `n`, or -1 if `m` is greater than `n`. The average is calculated by taking the average of `n` and `m`, and the binary representation is returned after the average is rounded to the nearest integer. 

The code includes a test suite that can be used to validate the functionality of the `rounded_avg` function:
```python
# Tests
assert rounded_avg(1, 5) == "0b11"
assert rounded_avg(7, 5) == -1
assert rounded_avg(10, 20) == "0b1111"
assert rounded_avg(20, 33) == "0b11010"
assert rounded_avg(3, 8) == "0b101"
assert rounded_avg(2, 5) == "0b101"
assert rounded_avg(1, 10) == "0b101010"
assert rounded_avg(10, 5) == -1
```