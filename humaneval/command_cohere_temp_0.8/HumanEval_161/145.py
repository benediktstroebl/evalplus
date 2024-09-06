```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(set(s).intersection(letters)) == 0 else ''.join(c.swapcase() if c in letters else c for c in s)
```
This Python script defines a function `solve` that takes a string `s` as input. The function inspects each character in the string using a generator expression. If the character is a letter, it toggles its case using the `swapcase` method. If the character isn't a letter, it remains unchanged. Finally, the function returns the modified string. This behavior is outlined in the function's docstring, which also provides example scenarios and their expected outcomes.