Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    bin_str = "{0:b}".format(n)
    sum_str = "".join(bin_str.split('1'))
    return sum_str
```
This script defines a function `solve(n)` that takes a positive integer `n` as input and returns the total sum of its binary digits.

The function uses the `format` function with a binary specification (`{0:b}`) to convert the number to a string representing its binary equivalent.

It then uses the `join` method to concatenate the string `1` that was used for splitting to ensure that all digits are treated as separate strings.

The resulting string `sum_str` contains each digit of the binary representation, which are to be summed. The function returns this summed string. 

This solution efficiently solves the problem in a self-contained manner, providing the total sum of a positive integer's digits in binary form.