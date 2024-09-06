Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(bit)) for bit in s if bit != '0'])
```
This function takes a positive integer `n` as input and converts it to a string. It then iterates over each character in the string, converting them to integers and filtering out the '0's. The filtered integers are then concatenated to form a binary string representing the total sum of the digits in binary. The function returns this binary string.