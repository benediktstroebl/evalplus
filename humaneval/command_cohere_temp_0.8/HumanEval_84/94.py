Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(int(''.join(s)))
```
This function takes a positive integer `n` as its argument and converts it to a string `s`. It then joins this string together to form a binary string, which is then converted back to an integer using the `int()` function. Finally, this integer is formatted as a binary string using the `format()` method and returned as the solution.