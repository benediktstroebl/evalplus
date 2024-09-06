Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s[:, :-5].translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'ijklmnopqrstvwxyzabc'))
```
The `encode_shift` function shifts every character by 5 in the alphabet. This is achieved via the expression `((ord(ch) + 5 - ord("a")) % 26) + ord("a")`, which gets the decimal value of a character, increases it by 5, subtracts the value of 'a' to just shift the letter, then takes a modulus of 26 to avoid skipping letters, and finally adds the value of 'a' back to get the shifted character's decimal value and returns the character.

The `decode_shift` function aims to reverse the encoding process and return the original string. The expression `s[:, :-5]` removes the first character of every word to remove the encoding. ``.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'ijklmnopqrstvwxyzabc'))`**` then translates each character back to its original state. `str.maketrans` returns a translation table based on the supplied pairs of strings. It is important to use `str.maketrans` and not map for the translation as `map` will return a list which will break the `translate` function.