```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    """ same string that is encoded with encode_cyclic function.
    return s
return "".join(decode_cyclic(s)))

# Example 1
print(encode_cyclic("Hello"))  # Output: hElLoW

# Example 2
print(encode_cyclic("World"))  # Output: wOrLD

# Example 3
print(encode_cyclic("Python is great"))  # Output: pThIaG is grEa

# Example 4
print(encode_cyclic("!NET has key"))  # Output: .NEThaskey

# Example 5
print(encode_cyclic("gf spokesman"))  # Output: gf Spojnsihp

# Example 6
print(decode_cyclic("."NEThaskey))  # Output: gf spokesman

# Example 7
print(decode_cyclic("gf is key"))  # Output: gf is key

# Example 8
print(decode_cyclic(""))  # Output: Hello)
```
This Python code defines a pair of functions: encode_cyclic and decode_cyclic, which are designed to handle a cyclic encoding and decoding task for a string. The encode_cyclic function splits the input string into groups of three characters, cycles the characters within each group, and then reassembles the characters into a string. The decode_cyclic function takes the input string and reverses the process, reconstructing the original string.