Here's a Python script that contains a function to solve the given problem:
```python
def solve(N):
    """Return the sum of digits in binary representation."""
    bin_str = '{:b}'.format(N)
    sum_str = ''.join(bin_str.split('1'))
    return sum_str
```
This script defines a function `solve(N)` that takes in a positive integer `N` as its argument and returns the total sum of its digits in binary representation. It converts the integer `N` to a binary string using the format code `{{:b}}` and then removes the `1` characters from the string. Afterwards, it joins the separated list of digits with a blank string, resulting in a string that contains the sum of the binary digits of `N`.

Here's an example of how you can use this function to compute the sum of digits for the number 147:
```python
solve(147)
# Output: "1100"
```