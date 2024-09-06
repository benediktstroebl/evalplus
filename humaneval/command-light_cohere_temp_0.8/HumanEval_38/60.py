```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = [sub[:3] + sub[3:] for sub in s.
    # cycle elements elements in each group. Unless group has fewer elements than 3.
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   ). support Test decoded string
   
    """
    return "".join(decode_cyclic(input_string))
```

This script defines a self-contained function that performs the encode_cyclic operation. The encode_cyclic function splits the input string into groups of length 3 and then cycles the characters in each group. The function then joins these groups together to form the decoded string. The decode_cyclic function takes the encoded string as input and calls the encode_cyclic function to decode it.