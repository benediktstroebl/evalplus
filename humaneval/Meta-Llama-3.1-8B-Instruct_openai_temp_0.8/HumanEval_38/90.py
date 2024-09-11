### Cyclic Encoding and Decoding in Python
#### Problem Statement
Implement a function that encodes a string by cycling groups of three characters, and a function that decodes the encoded string back to its original form.

#### Solution

```python
def encode_cyclic(s: str) -> str:
    """
    Encodes the input string by cycling groups of three characters.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # Split the string into groups of three characters.
    # Use list comprehension to ensure the last group has the remaining characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle the elements in each group, unless the group has fewer elements than three.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join the groups into a single string and return the result.
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Decodes the input string that was encoded using the encode_cyclic function.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Split the string into groups of three characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Re-cycle the elements in each group back to their original order.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    # Join the groups into a single string and return the result.
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdefghij")
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements in each group, and returns the encoded string. The `decode_cyclic` function takes the encoded string as input, reverses the cycling process, and returns the decoded string.

In the example usage section, we demonstrate how to use these functions by encoding the string "abcdefghij" and then decoding the resulting encoded string back to its original form.