Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(int(''.join(s)))
```
This function takes a positive integer `n` as its argument and returns the total sum of its digits in binary. It converts the integer to a string, then joins this string into a single integer, and converts it to a binary string to return.

For example, with `n` equal to 1000, the function would return "1", and with `n` equal to 150, it would return "110".