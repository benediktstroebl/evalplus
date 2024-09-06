```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    Args:
        s (str): input string

    Returns:
        encoded string
    """
    return s.h([(3 * i):min((3 * i + 3), len(s)) - 2) for i in range((len(s) + 2) // 3)]

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    traditional decoding
   """
    return s.decode(''.