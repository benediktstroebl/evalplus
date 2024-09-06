Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    # Find the average
    total = (m + n) // 2
    # Round the average to the nearest integer
    avg = int(round(total))
    # Convert to binary
    return f"0b{bin(avg)[2:]}"
```

The `rounded_avg` function takes in two integers `n` and `m` as parameters. If `n` is greater than `m`, it returns -1. If not, it calculates the average of the two numbers and rounds it to the nearest integer. Finally, it converts the result to a binary string, and returns it.

The script passes the tests outlined in the problem statement:
```python
# TEST CASES
assert rounded_avg(1, 5) == "0b11"
assert rounded_avg(7, 5) == -1
assert rounded_avg(10, 20) == "0b1111"
assert rounded_avg(20, 33) == "0b11010"
```

To test it further, one could write more tests for corner cases such as `rounded_avg(0, 333)`, `rounded_avg(333, 0)`, and so on.