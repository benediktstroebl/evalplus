Here's a Python script that contains a function to solve the given problem:
```python
def solve(N):
    s = str(N)
    return '{0:b}'.format(sum(int(d) for d in s))
```
This function takes a positive integer `N` as its argument and returns the total sum of its digits in binary. It converts the integer `N` to a string `s` and uses a format specifier `{{:b}}` to convert each digit of the string to its binary representation. It then finds the sum of these binary digits using a generator expression `int(d) for d in s` and converts it to a binary string using the format specifier `{{:b}}`.  The result is then returned as a binary string.