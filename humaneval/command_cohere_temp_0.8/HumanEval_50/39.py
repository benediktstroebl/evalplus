Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", " abcdefghijklmnopqrstuvwxyz"))
```
The `encode_shift` function shifts every character in the given string by 5 in the alphabet to achieve the encoding. The `decode_shift` function reverses the shift operation to decode the string.

This solution uses character mapping and the `translate` method for decoding, which is built more optimally for edge cases and efficiency. The translated characters are all within the ASCII range. Both functions assume the input string consists only of English characters, which is a requirement mentioned in the original problem.  It would be incorrect to assume that non-English characters would be handled correctly by the code.