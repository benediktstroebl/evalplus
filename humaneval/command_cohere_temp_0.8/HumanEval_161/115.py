```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz':]
```
The function relies on the `swapcase()` method, which swaps the case of letters in a string, to solve the problem. This approach reverses the entire string if it doesn't contain any letters, and otherwise, it reverses only the letter characters while keeping non-letter characters unchanged.