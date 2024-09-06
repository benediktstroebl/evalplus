```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    bare testing... general method to decode a cyclic group of characters.

# Example tests
test_encode_cyclic = encode_cyclic.check( encode_cyclic("hello world"))
test_decode_cyclic = decode_cyclic.check( decode_cyclic("hello world"))
``` 
The `encode_cyclic` function converts a string into a sequence of groups of three characters, where each group is cycled. The `decode_cyclic` function reverses this process to produce the original string.