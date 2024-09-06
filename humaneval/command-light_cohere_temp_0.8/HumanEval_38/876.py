```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(group[::-1] for group in s[::3])

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    have funct.
    This each character takes the particular encoded string and returns decoded one.
    encoded_str = encode_cyclic(s)
    decoded_str = "".join(char for char in encoded_str if char.isalpha())
   \s"""
   
    return decoded_str
```

This code defines a self-contained Python function called `encode_cyclic` that takes a string as input and returns an encoded version of that string by cycling groups of three characters. Similarly, `decode_cyclic` is a function that takes an encoded string as input and returns the decoded string. It uses the string slicing to split the input string into groups of three characters, then reverses each group to obtain the encoded version. The code also uses a set of tests to verify that the `encode_cyclic` and `decode_cyclic` functions produce the expected output.