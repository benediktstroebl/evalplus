Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(int(''.join(s))).replace('0b', '')
```
This function takes a positive integer `n` as input and converts it to a string `s`. It then joins the string together to form a binary string and converts it to an integer. The binary string is returned, with the '0b' prefix removed, giving the total sum of digits in binary format.