Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(sum(int(d) for d in s))
```
This function takes a positive integer `n` as its argument and returns the total sum of its digits in binary. It converts the integer to a string, `s`, and then uses a format specifier `{{:b}}` to convert the sum to a binary string. The sum is calculated by iterating through the digits of the string and converting them to integers.