```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters]
```
The function takes a string and checks if the characters are letters or not using set comparisons and the `swapcase()` method to swap the case of characters. If all characters are letters, it simply swaps the case of all characters. Otherwise, it swaps the case of characters that are not letters.