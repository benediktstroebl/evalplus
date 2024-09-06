Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    s = str(n)
    return bin(sum(int(d) for d in s))[2:].zfill(32)
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string `s`, and then uses a generator expression within the sum function to convert each digit to an integer. Then it converts the result to binary and pads it with leading zeros to a length of 32 bits, so it is a full binary string. 

You can test this function by calling it with any integer between 0 and 10,000, such as `solve(150)`, which should return "110" as the sum of its digits in binary.  This solution has an time complexity of O(log(N)) and a space complexity of O(1) as it only uses a variable to convert the number to a string for the moment for doing the summation.