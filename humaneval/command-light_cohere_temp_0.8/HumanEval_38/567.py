```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    return ["".join(c) for c in groups] + s[::-1]

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    pattern matching with encode_cyclic function.
    return s.join(groups) 
```

The encode_cyclic and decode_cyclic functions take a string s as input and return a new string. The encode_cyclic function uses a 3-character pattern matching to cycle groups of three characters together, and the decode_cyclic function uses the same pattern matching to reverse the original string. The code is a self-contained and does not rely on any external functions or classes.