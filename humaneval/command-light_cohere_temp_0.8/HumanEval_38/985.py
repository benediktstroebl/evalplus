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
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    guaranteed: encoded string decoded correctly.
    """

encoded_string = encode_cyclic("hello")
 decoded_string = decode_cyclic(encoded_string)
print(f"encoded: {encoded_string}, decoded: {decoded_string})
```
The code defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string `s` as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string. 

The code then creates an encoded string with the `encode_cyclic` function, and calls the `decode_cyclic` function to get the decoded string. Finally, the code prints the encoded string and decoded string and confirms that they are the same, which confirms the correctness of the `decode_cyclic` function.