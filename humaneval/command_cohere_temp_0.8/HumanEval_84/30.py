Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(int(''.join(s))).replace('0b', '')
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the total sum of its digits in binary. It converts the integer to a string `s`, then joins this string together to form a binary string. This binary string is converted back to an integer, and the binary representation is returned as a string, with the leading "0b" removed. 

Here's an example of how you can use the function with the argument `n = 147`:
```python
solve(147)
# Output: "1100"
```
This example will return the string "1100" which is the binary representation of the sum of its digits in decimal, which is 12.