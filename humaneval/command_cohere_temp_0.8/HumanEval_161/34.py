```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[0::2 if c.isalpha() else 1 for c in s]
```
The function uses `swapcase()` to handle no-letter and all-letter cases in one pass. The `set()` function is used to check if the string contains any letters. The `indexing` logic is done using a generator expression, leveraging Python's ability to slice and conditionally iterate without creating a new array. The `isalpha()` method is used to check if the character is a letter or not, and depending on the result, a character is either reversed every two times (if it's a letter) or every single time it appears in the string.