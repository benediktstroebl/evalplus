Here's a Python script that includes a function to solve the given problem:
```python
def solve(N):
    s = str(N)
    return '{0:b}'.format(int(''.join(s)))
```
This function takes a positive integer `N` as input and converts it to a binary string. It does this by first converting `N` to a string using `str(N)`, then joining this string together to form a binary string using `int(''.join(s))`. Finally, it formats this binary number in binary notation using the `format` function with a prefix of `0b` and returns the result as a string. 
This solution directly addresses the problem statement and provides a function to achieve the desired output.