Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i: i+3]) ^ int(s[i+2: i+5])) for i in range(0, len(s), 3)])
```
The function `solve` takes a positive integer `n` as its argument and returns the binary string that is the sum of its digits. It converts the integer to a string, and then iterates over it in steps of 3 characters. Using bitwise XOR, it converts each triplet of digits into a single binary digit and returns the resulting binary string. 

This approach leverages binary digits' properties where XORing two digits (their positions in the binary representation) results in a value that equals the XOR of the two digits' values.

The `solve` function is self-contained and can be easily reused to calculate the sum of digits for any positive integer up to 10,000, returning it as a binary string.