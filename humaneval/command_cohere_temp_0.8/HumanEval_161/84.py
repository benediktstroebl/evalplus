```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s` which takes a string `s` as input and performs the desired operations as mentioned in the problem statement. It iterates through each character `c` in the input string `s` and uses the `isalpha()` method to check if it's a letter. If it is, the `swapcase()` method is used to swap its case, converting it to the opposite case of the original. If the character is not a letter, it's kept as-is without any changes. Finally, the function returns the resulting string by joining the modified characters together.