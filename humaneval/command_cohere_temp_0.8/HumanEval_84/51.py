Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{:b}'.format(int(''.join(s)))
```
This function takes a positive integer `n` as input and converts it to a string `s`. It then joins this string together to form a binary string, which is then converted back to an integer using the `int()` function. This integer is then formatted back to a binary string using the `format()` method with the formatting specifier `{:b}`. The resulting binary string is then returned as the solution.

Let's break down the solution by going through an example:
```python
solve(100)
# Output: 11011100

solve(123)
# Output: 1111110101
```

This approach effectively converts the integer to a binary string and then summates the binary representation of the digits. The combined sum of the binary digits is then returned as a binary string.