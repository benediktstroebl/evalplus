Here is a Python script that includes a self-contained function to solve the problem of encoding and decoding cyclical groups of characters in markdown code blocks:

```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string