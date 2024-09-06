```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(set(s).intersection(letters)) == 0 else s.translate(str.maketrans(letters, letters.swapcase()))
```
This Python script defines a function `solve` designed to transform a given string `s` in a specified manner. The function operates as follows: If the string contains no letters from the Latin alphabet, it is reversed using the `swapcase` method. Otherwise, each letter in the string is modified by reversing its case while leaving non-letter characters unchanged. This is accomplished using the `translate` method with a custom translation table created by `str.maketrans` to swap the cases of letters. The result is a modified string that fulfills the problem statement's requirements.