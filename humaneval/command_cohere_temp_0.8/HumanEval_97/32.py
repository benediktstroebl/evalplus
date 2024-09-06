```python
def multiply(a, b):
    return int(str(a)[-1]) * int(str(b)[-1])
```
This Python script defines a function `multiply` that takes two integer inputs `a` and `b` and returns the product of their unit digits. The unit digit is the digit at the end of the number when counting in Arabic numerals. The function uses the last character in decimal representation to make the calculation using `str(a)[-1]` and `str(b)[-1]`.  This is exemplified in the test cases provided. 
For example, in the test case `multiply(148, 412)`, the result is `16`, because the unit digits of `148` and `412` are `4` and `6` respectively, and `4 * 6 = 16`. 

The provided solution is clean and efficient, providing a clear and concise implementation of the problem description.