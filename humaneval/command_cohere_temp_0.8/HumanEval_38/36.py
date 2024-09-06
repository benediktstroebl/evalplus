```python
def encode_cyclic(s: str) -> str:
    """
    Encodes a string by cycling groups of three characters.
    """
    # Split string into groups of three (or shorter).
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle the elements in each group.
    groups = [group[1:] + group[0] for group in groups]
    return ''.join(groups)

def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.
    """
    # Split the string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Reverse the cycling effect.
    groups = [group[0] + group[2:] for group in groups]
    return ''.join(groups)
``` 

This script includes two functions `encode_cyclic` and `decode_cyclic` which accomplish the tasks of encoding and decoding respectively.

The `encode_cyclic` function takes a string `s` as input and returns a encoded string. It splits the input string into groups of three characters over padding with empty strings if needed. It then cycles each group - the group is reversed and concatenated with itself. This process is repeated for each group in the string and the results joined to form the final encoded string. 

The `decode_cyclic` function also takes a string `s` as input and returns the decoded string. It splits the input string into groups of three over padding with empty strings if needed. It then reverses the effect of the cycling for each group - the first character is removed and appended to the end of the group, thus undoing the encoding process. This process is carried out for each group in the string and the results joined to form the final decoded string. 

These functions operate solely on the string character indices and do not make use of any implicit global state. Hence, they are self-contained and can be called with a string as input to encode or decode that string. 

Note: the functions encode and decode assume the input string is a multiple of three characters long. If the string length is not a multiple of three, padding characters are ignored in the encoding/decoding processes.