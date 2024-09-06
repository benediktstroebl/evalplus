Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s][5:].translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdeghijklmnopqrstuvwxyz"))
```
The `encode_shift` function shifts each character of the input string `s` by 5 in the alphabet. The `decode_shift` function first removes the first 5 characters of the encoded string and then uses the `translate` function with a custom translation table to decode the characters back to their original values. This pair of functions should correctly handle the string encoding and decoding tasks required by the problem. 
The `decode_shift` function requires the input string `s` to be at least 5 characters long to properly decode the string, as the first 5 characters are removed to recover the original input. This is a check to ensure no incomplete or manipulated data poses a problem to the decoding function.