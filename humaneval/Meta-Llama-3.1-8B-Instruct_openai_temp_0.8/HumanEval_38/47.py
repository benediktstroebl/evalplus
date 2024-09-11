Here is a self-contained Python script that solves the problem:
```markdown
# Cyclic Encoding and Decoding Functionality
=============================================

### Overview

This script provides two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and encodes it by cycling groups of three characters. The `decode_cyclic` function takes a string encoded with `encode_cyclic` and returns the original string.

### Code

```python
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    # Split encoded string to groups of three characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Extract first character of each group and cycle other characters.
    decoded_groups = [(group[0] + group[1:]) if len(group) == 3 else group for group in groups]
    
    # Join decoded groups to form original string.
    return "".join(decoded_groups)


# Example usage
if __name__ == "__main__":
    original_string = "abcdefghi"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

### Explanation

The `encode_cyclic` function splits the input string into groups of three characters using list comprehension. It then cycles the elements in each group by moving the first character to the end of the group. If a group has fewer characters than three, it is left unchanged.

The `decode_cyclic` function performs the reverse operation. It splits the encoded string into groups of three characters and then moves the first character of each group to the beginning to restore the original order.