```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(set(s).intersection(letters)) == 0 else ''.join(c.swapcase() if c in letters else c for c in s)
```
This Python script defines a function `solve` that takes a string `s` as input. The function inspects each character in the string using a generator expression. If the character is a letter, it toggles its case using the `swapcase` method. If the character isn't a letter, it remains unchanged. Finally, the function returns the modified string. This process effectively flips the case of letters while leaving non-letter characters unchanged, thereby solving the problem statement.