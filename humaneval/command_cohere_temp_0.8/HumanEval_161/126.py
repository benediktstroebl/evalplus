```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(set(s).intersection(letters)) == 0 else ''.join(c.swapcase() if c in letters else c for c in s)
```
This Python script defines a function `solve` that takes a string `s` as input. The function inspects each character in the string using a generator expression. If the character is a letter, it uses the `swapcase` method to change its case, regardless if it is upper or lower case. If the character is not a letter, it remains unchanged. The function returns the resulting string after applying these rules to each character. This solution is concise and effectively accomplishes the problem requirements.