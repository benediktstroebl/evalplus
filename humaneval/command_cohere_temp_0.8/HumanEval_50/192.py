```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "oricbfghijkmnopqstuvwxyza"))
```
The `decode_shift` function uses the `translate` method to shift each character back to its original position. The `maketrans` function creates a translation table that maps each character in the encoded string to its original position in the alphabet. 
This approach avoids the need for manually iterating through the string and results in a more concise and efficient solution.