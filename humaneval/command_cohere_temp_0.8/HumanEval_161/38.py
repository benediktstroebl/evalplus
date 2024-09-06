```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking a single argument `s`, which performs the desired string transformations as specified in the problem statement. Here's how this code works:
1. The function `solve` iterates over each character `c` in the input string `s`.
2. It checks if each character `c` is an alphabetic character using the `isalpha()` method.
3. If `c` is an alphabetic character, it uses the `swapcase()` method to swap its case, converting it to either uppercase or lowercase. This operation leaves non-alphabetic characters unchanged.
4. For non-alphabetic characters, the loop simply retains the character as is.
5. Finally, the function returns the resulting string after applying the transformations to each character.