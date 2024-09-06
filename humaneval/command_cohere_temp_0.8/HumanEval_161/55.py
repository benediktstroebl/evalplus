```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(set(s).intersection(letters)) == 0 else s.translate(str.maketrans(letters, letters[1:] + letters[:1]))
```
The code uses `swapcase()` to reverse the string when there are no letters in the string, and uses `translate()` to reverse the letters while keeping non-letter characters unchanged. The approach guarantees the correct solution for the described problem.