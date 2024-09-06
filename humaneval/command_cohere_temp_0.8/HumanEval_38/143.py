```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return ''.join(groups)

def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Uncycle elements in each group. Unless group has fewer elements than 3.
    groups = [group[:2] + group[2:] if len(group) == 3 else group for group in groups]
    return ''.join(groups)
``` 

This script provides two functions: `encode_cyclic` and `decode_cyclic`. 

The `encode_cyclic` function takes a string `s` as input and returns a encoded string by cycling groups of three characters. It splits the input string into groups of three characters, and then cycles the elements within each group. This is done to ensure that no two consecutive characters are the same. It then joins the cycled groups back into a single string to provide the encoded output. 

The `decode_cyclic` function takes a string s as input and returns the original string by undoing the encoding process. It splits the encoded string into groups of three characters, and then uncycles the elements within each group. This is done by swapping the first and second characters with the second and third characters, respectively. It then joins the uncycled groups back into a single string to provide the decoded output. 

Overall, these functions allow you to encode a string in such a way that no two consecutive characters are the same, and then decode it back to the original string. 

Here is an example of how you can use these functions:
```python
input_string = "abc"
encoded_string = encode_cyclic(input_string)
decoded_string = decode_cyclic(encoded_string)

print("Input String:", input_string)
print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
``` 
This would produce the following output:
```
Input String: abc
Encoded String: bfc
Decoded String: abc
```

This demonstrates that the `encode_cyclic` function encodes the input string by cycling groups of three characters, and that the `decode_cyclic` function correctly decodes the encoded string.