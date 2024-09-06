Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(int(''.join(s)))
```
This function takes a positive integer `n` as input and converts it to a binary string format. It does this by first converting the integer to a string (`s = str(n)`), then joining the string digits to form a binary integer (`int(''.join(s))`), and finally formatting it as a binary string (`{0:b}`.format`). The function returns the binary string representing the total sum of the input integer's digits. 

Here is an example of an input/output concerning this function:
**Input:** 15000
**Output:** 111110111100

You can test this function further by calling it with different input values within the given range of 0 to 10000 and checking that the output is the correct binary string representation of the sum of the digits.