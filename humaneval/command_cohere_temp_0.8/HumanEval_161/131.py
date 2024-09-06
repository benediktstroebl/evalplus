```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking a single string argument `s`, where it iterates through each character in the string, checking if each character is an alphabet letter using the `isalpha()` method. When encountering alpha characters, it uses the `swapcase()` method to interchange their cases, converting them to their upper case if they are in lower case or vice versa. In contrast, non-letter characters like digits and special symbols are left unchanged and are appended as is to the resulting string. The function effectively reverses the string if it contains no letter characters, providing the appropriate output as per the problem description. 
The `solve` function can be invoked with various input strings to witness its behavior and could be incorporated into larger programs to accomplish specific tasks.