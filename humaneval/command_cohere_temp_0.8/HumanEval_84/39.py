Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(sum(int(d) for d in s))
```
This function takes a positive integer `n` as its argument and returns the total sum of its digits in binary. It converts the integer to a string, iterates through its digits, converts them to integers, and sums them. Finally, it uses `format` with `{0:b}` to convert the sum to a binary string and returns the result.