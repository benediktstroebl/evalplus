Here is a Python script that contains a self-contained function that solves the problem you provided:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   
recursively
    """
    return s.decode_cycl()
recursive. The recursive version of the decode function. The decode function calls itself with the string "". decoded_str and returns the decoded string when it has at least three characters (a length of 3). This will ensure that the recursive function will eventually reach the decoded string.

Now, we can run the encode and decode functions to test their correctness.