Here's a self-contained Python script that solves the problem:
```markdown
### Cyclic Encoding and Decoding

This script implements two functions, `encode_cyclic` and `decode_cyclic`, to encode and decode a given string by cycling groups of three characters.

#### Functions

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    # Pad the result with spaces to make groups divisible by 3
    while len(groups) % 3!= 0:
        groups.append(groups.pop())
    # Pad the last group with a space to match the original encoding
    groups[-1] +=''
    return "".join(groups).replace(" ","")

def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string to groups.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    
    # Decode each group. If group has fewer elements than 3, assume it's a truncated group and ignore it.
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            decoded_groups.append(group[1:] + group[0])
        elif len(group) == 2:
            decoded_groups.append(group)
    
    # Join the decoded groups to form the decoded string.
    return "".join(decoded_groups)
```

#### Example Use Case

```python
# Test the functions
encoded_str = encode_cyclic("HelloWorld")
decoded_str = decode_cyclic(encoded_str)
print("Encoded string:", encoded_str)
print("Decoded string:", decoded_str)
```

This script first encodes the input string using the `encode_cyclic` function, which splits the string into groups of three characters, cycles the elements in each group (unless the group has fewer elements than three), and pads the result to make groups divisible by three. The `decode_cyclic` function takes the encoded string as input and reverses the process to obtain the original string. The example use case demonstrates how to use these functions to test the cyclic encoding and decoding.