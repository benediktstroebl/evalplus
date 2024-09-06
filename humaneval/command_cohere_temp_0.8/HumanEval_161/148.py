```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s`, where based on the problem statement description, it iterates through each character `c` in the string `s`. For each character, it checks if it is alphanumeric using the `isalpha()` method. If true, it swaps its case using the `swapcase()` method, which changes the character to either upper case if it is in lower case or lower case if it is in upper case. If it is not true, it keeps the character as is and includes it in a string concatenation denoted by `''.join()`. Ultimately, the function returns the resulting string that has been reversed and had its case corrected for alphanumeric characters.