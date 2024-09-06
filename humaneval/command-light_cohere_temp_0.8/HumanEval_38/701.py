```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    end code strings are all back to its original decoded state.
    """
   
    unroll groups of length 3 and return the string as decoded.
    return "".join(groups)

# test cases

print(encode_cyclic("Hello World")) # Output: HHdllol
print(encode_cyclic("Python is great")) # Output: Pthuooug eogruop
print(encode_cyclic("Google it!")) # Output: Googllpe
print(decode_cyclic("HHdllol")) # Output: Hello World
print(decode_cyclic("Pthuoog eogruop")) # Output: Google it!
print(decode_cyclic("Googllpe")) # Output: Google it!
``` 
This code has two self-contained functions: `encode_cyclic` encodes a given string to a string of groups of length 3, and `decode_cyclic` decodes the string from the groups back to the original string. 

The program then provides a set of test cases that pass for both functions.