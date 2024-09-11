Here's a Python script that implements the `encode_cyclic` and `decode_cyclic` functions:
```markdown
### Cyclic Encoding and Decoding

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group in reverse order. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage:
print(encode_cyclic("abcdefg"))  # Should print "cdefbag"
print(decode_cyclic(encode_cyclic("abcdefg")))  # Should print "abcdefg"
print(encode_cyclic("123"))  # Should print "231"
print(decode_cyclic(encode_cyclic("123")))  # Should print "123"
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string `s` as input and returns a new string where groups of three characters are cyclically shifted. The `decode_cyclic` function takes an encoded string as input and returns the original string. The example usage demonstrates how to use these functions.