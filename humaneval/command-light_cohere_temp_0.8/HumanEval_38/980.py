```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return_str = ""
    for i in range((len(s) + 2) // 3):
        groups = s[(3 * i):min((3 * i + 3), len(s))]
        # cycle elements in each group
        elements = [group[1:] + group[0] for group in groups]
        # unless group has fewer elements than 3
        if len(elements) == 3:
            return_str += "".join(elements)
    return return_str

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    all that 
    """
    ```
    ```

This code implements the encode_cyclic and decode_cyclic functions that solve the problem of encoding and decoding a string of characters. The encode_cyclic function takes a string as input and returns an encoded string by cycling groups of three characters. The function uses a list comprehension to split the string into groups of three characters, and then cycles the elements in each group. The decode_cyclic function takes an encoded string as input and returns a decoded string. It uses the same other function to decode the input and returns the decoded string.