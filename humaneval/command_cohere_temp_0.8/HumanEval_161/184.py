```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) else s[::-1]
```
The function `solve` takes a string `s` as input and first checks if there are any letters in the string using the `set` function and creating a letter set for comparison. If there are no letters, it uses the `s[::-1]` slice to reverse the entire string. If there are letters, it uses the `swapcase` method to reverse the case of letters while keeping non-letter characters unchanged. This solves the problem for the corner case of strings containing no letters as well as for letters present in the string.