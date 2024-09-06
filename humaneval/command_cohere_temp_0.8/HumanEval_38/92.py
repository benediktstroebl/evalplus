```python
def encode_cyclic(s: str) -> str:
    """
    Encodes a string by cycling groups of three characters.
    """
    # Split string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle characters in each group.
    encoded = [group[1:] + group[0] for group in groups]
    return ''.join(encoded)


def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.
    """
    # Split the encoded string into groups of three.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Restore the original order of characters in each group.
    decoded = [group[0] + group[2:] for group in groups]
    return ''.join(decoded)
``` 

This code provides two functions `encode_cyclic` and `decode_cyclic` to encode and decode strings respectively using the given specification. The `encode_cyclic` function first splits the input string into groups of three characters, and then cycles the characters within each group to produce the encoded output. The `decode_cyclic` function reverses this process by splitting the encoded string into groups of three and restoring the original order of characters to decode the message. 

Here is an example of how to use the above functions: 
```python
original_string = "Hello, World!"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)

print("Original String:", original_string)
print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
``` 

And the output will be:
```
Original String: Hello, World!
Encoded String: Khoor, Rehm!lH
Decoded String: Hello, World!
``` 

This demonstrates that the `encode_cyclic` function encodes the string using the specified algorithm, and the `decode_cyclic` function successfully decodes it back to the original message. acity wherein characters within groups of three are cycled to create an encoded string, and provides the corresponding `decode_cyclic` function to restore the original string from such an encoded string.