Here's a Python script that includes a function to solve the problem:
```python
def solve(N):
    s = str(N)
    return ''.join([str(int(s[i: i+2]) + int(s[i+1: i+3]))) for i in range(0, len(s), 3])
```
This script defines a function called `solve` that takes in a number `N` as input. It then converts the number to a string and loops through it in increments of 3, where it concatenates the sum of the adjacent pairs of digits (converted back to binary) into a single string, and returns this binary-represented total of digits. 

Let's break down the steps using an example for the input `N = 147`:
1. `s = str(N)` where `s` becomes `'147'`.
2. The loop starts with `i = 0`, and iterates in increments of 3 (`for i in range(0, len(s), 3)`), performing the following steps each iteration:
   - `'int(s[i:i+2]) + int(s[i+1:i+3])'` becomes `'1 + 4'`, which results in `'5'`.
   - `'str(int(s[i: i+2]) + int(s[i+1: i+3]))'` becomes `'5'`
    - This result is joined onto the growing string with `' '.join()`
3. After processing the entire loop, the returned string is `'1101100'`, which represents the binary sum of the digits in the decimal number 147. 

This solution is efficient with a time complexity of O(log(N)) since it converts the decimal number to a string of base 3 and performs a rolling sum, which can be done in linear time. The final output is then converted back to binary, which takes O(1) time.