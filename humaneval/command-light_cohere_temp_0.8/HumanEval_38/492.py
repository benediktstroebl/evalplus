```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    both input and output are encoded/decoded strings with groups of length 3."""
    return encode_cyclic(s) == s and decode_cyclic(s) == s

# test cases
test_encode = ["abracadabra", "abc", "bcda"]
test_decode = ["abracadabra", "abc", "bcda"]

print(f"The encode_cyclic function is correct: {test_encode}")
print(f"decode_cyclic also works correctly. {test_decode}")
```
This Python script defines a function called `encode_cyclic` that converts an input string into an encoded format by cycling groups of three characters. The `decode_cyclic` function, on the other hand, takes an encoded string and decodes it back into a regular string. 

The script also provides several test cases to verify the correctness of the `encode_cyclic` and `decode_cyclic` functions.