Here's the provided Python script:
```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters each
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    elements = [group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(elements)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   aya
   
    Uncommenting code below is a duplicate of the above description.
``` 
The code has two functions:
1. `encode_cyclic`: This function splits a string into groups of three characters each and cycles the elements in each group. The resulting encoded string will be returned.
2. `decode_cyclacycl`: the function takes the input string and returns the decoded string by un-cancelling the elements of the encoded string.