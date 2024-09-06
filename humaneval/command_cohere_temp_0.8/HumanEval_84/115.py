Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1]) ^ 1) for i in range(len(s))])
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the binary string digit-wise sum of the digits of the input number `n`. It converts the integer to a string, iterates over each digit, and converts it to binary by taking its complement. The resulting binary digits are joined to form the output binary string representing the sum of the digits in binary. 

The code is self-contained and can be executed directly to test it. You can use it in your solution or modify it to suit your needs.