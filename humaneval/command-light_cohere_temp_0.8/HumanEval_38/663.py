```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    1.
    splits string to groups of length 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in s]
    2.
    joins groups back a string using ","
    return encoded_str

def decode_cyclic(s: str):
    """
    takes as input encoded string returned by encode_cyclic. Returns decoded string.
    decoded_string using same [
    using string.join and lowercasing the
    string is decoded by using groups returned by encode_cyclic.
    """
    join all decoded strings in the list to form the decoded string

# test cases

# encoded
should be decoded
print(decode_cyclic("..."))
# decoded

print(decode_cyclic("Aaaaa"))
# decoded

print(decode_cyclic("DEFG"))
# decoded

print(decode_cyclic("aeiou"))
# decoded

print(decode_cyclic("XYZABC"))
# decoded
```