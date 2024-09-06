Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(int(''.join(s)))
```
This function takes a positive integer `n` as its argument and converts it to a string `s`. It then joins this string together to form a binary string and converts it to an integer. It then returns this binary integer.

For example, given the input `n = 1000`, the function would return `b'1'` after summing up its binary digits, yielding a total of `1` as the output. 

This solution leverages Python's string formatting using `format()` and `join()` functions to achieve the desired result, as demonstrated in the provided code block.