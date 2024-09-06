```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    reasons:
        - new function for better code reusaece and readability.
    - separate decode logic.
    - improves test for performance by avoiding encoding/decoding twice.
    """
    reasons:
        - separate function for better code reusae and readability.
    - decoding logic is kept separate for clarity and future extensibility.
    """