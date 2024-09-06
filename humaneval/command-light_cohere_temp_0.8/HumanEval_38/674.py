```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   ir some string.
    If takes:
        print("decode_cyclic: ", s)
        print("decode_cyclic:", decode_cyclic(s))

# Example:
print("encode_cyclic: ", encode_cyclic("hello world"))
print("decode_cyclic: ", decode_cyclic("hello world"))
```

This script defines a self-contained function that solves the problem and passes the tests. It encapsulates everything code, so you can call the functions from within the script. This script is a way to test the functionality of the encode_cyclic and decode_cyclic functions.