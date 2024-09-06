Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1]) ^ 1) for i in range(len(s))])
```
This function takes a positive integer `n` as its argument and calculates the sum of its digits in binary. It converts the integer to a string, `s`, and then loops through its characters, taking advantage of the fact that converting a number to binary is the same as converting its digits to binary. It uses bitwise XOR with 1 to convert each digit to its binary representation. The resulting binary digits are then concatenated to form the final binary string representation of the sum.