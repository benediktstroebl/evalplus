```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(set(s).intersection(letters)) == 0 else s.translate(str.maketrans(letters, letters[1:1:-1]))
```
The `swapcase` method is used to invert the case of characters in a string. However, this method does not handle non-alphabetical characters and treats them as unaffected. To handle these characters separately, the approach replaces alphabetical characters with their mirrored counterpart using the `translate` method and `str.maketrans`. This inversion mechanism ensures that non-alphabetical characters remain untouched. The result is a string with flipped alphabetical characters and unchanged non-alphabetical characters.