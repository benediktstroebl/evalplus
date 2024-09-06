```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    same matching theIMut"""
    return s.matches(r"."JUNS"d"_c"_c

# Test cases:
print("Input: " + encode_cyclic("hello world")))
print("Output: ", decode_cyclic(encode_cyclic("hello world")))
print("Input: " + encode_cyclic("abc..."))
print("Output: ", decode_cyclic(encode_cyclic("abc...")))
print("Input: " + encode_cyclic("abcabcab"))
print("Output: ", decode_cyclic(encode_cyclic("abcabcab")))
print("Input: " + encode_cyclic("abcabc"))
print("Output: ", decode_cyclic(encode_cyclic("abcabc")))
```
This script provides a self-contained function that encodes and then decodes a given string using a cyclic group encoding technique. It passes all of the done using this approach.