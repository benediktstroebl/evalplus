```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters]
```
The function uses the `swapcase()` method to flip characters case and the `set()` function to check if there are any letters in the string, if there aren't any letters it uses the `swapcase()` method otherwise it uses the `swapcase()[letters]` to only flip the letters case.