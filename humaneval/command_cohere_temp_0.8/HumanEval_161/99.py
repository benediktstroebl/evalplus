```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[0::2 if c.isalpha() else 1 for c in s]
```
The function relies on Python's string method swapcase to handle the case-reversal of non-letter characters correctly, as per the requirement. The conditional iteration [0::2 if c.isalpha() else 1 for c in s] ensures that every character in the string goes through the swapcase function if it's a letter, and skips it if it isn't. This approach avoids the need for a custom reversal function and makes the code more concise and maintainable.