### Cyclic Encoding and Decoding

Here's the complete Python script for the `encode_cyclic` and `decode_cyclic` functions:

```markdown
### Cyclic Encoding and Decoding

This script provides two functions: `encode_cyclic` and `decode_cyclic`. 
The `encode_cyclic` function takes a string as input, splits it into groups of three, 
cycles the elements in each group unless the group has fewer elements than three, 
and returns the encoded string.

The `decode_cyclic` function takes the encoded string as input and returns the decoded string.

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode each group by cycling elements back to their original position
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    # Test the functions
    original_string = "abcdef"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
    
    # Check if the decoded string matches the original string
    assert decoded_string == original_string, "Decoding failed"
    print("Decoding successful")
```

### Explanation:

- The `encode_cyclic` function splits the input string into groups of three characters and cycles the elements in each group by moving the first element to the end.
- The `decode_cyclic` function does the opposite, cycling the elements back to their original position.

- Note that the `decode_cyclic` function uses a similar approach as `encode_cyclic`, but instead of moving the first element to the end, it moves the last element to the front to reverse the effect of cycling.