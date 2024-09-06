```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
        main test code:
    ```
    test cases:
    encode_cyclic "hello" # Output: "h.w"
    encode_cyclic "world" # Output: "dlrow"
    encode_cyclic "abcba" # Output: "cmkmkm"
    encode_cyclic "abcdef" # Output: "fghjih"
    decode_cyclic("h.un"  # Output: "hello"
    decode_cyclic("dloww"  # Output: "hello"
    decode_cyclic("cmkmkm"  # Output: "world"
    decode_cyclic("fghjih"  # Output: "abcdef"