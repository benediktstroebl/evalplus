Here's a Python script that includes a function to solve the given problem:
```python
def solve(N):
    """Returns the sum of digits in binary representation of the integer N."""
    bin_str = '{:b}'.format(N)
    return bin_str.count('1')
```
This script defines a Python function `solve(N)` that takes an integer `N` as input and calculates the sum of its binary digits. The function uses the format specification `{:b}` to convert the integer `N` to a string representing its binary equivalent. It then counts the number of occurrences of the digit '1' in this binary representation and returns this count, which provides the desired sum of the digits.