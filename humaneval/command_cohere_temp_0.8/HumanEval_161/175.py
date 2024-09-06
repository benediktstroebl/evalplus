```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s` which takes a string and operates on it as per the problem statement. It returns the modified string as the result. 

The function uses a `for` loop that iterates over each character `c` in the input string `s`. For each character, it checks if it is an alphabetic character using the `isalpha()` method. If it is, it uses the `swapcase()` method to change the case of the character. If it's not, it retains the character as is. Finally, the output string is created by concatenating all the modified characters using the `join()` method.