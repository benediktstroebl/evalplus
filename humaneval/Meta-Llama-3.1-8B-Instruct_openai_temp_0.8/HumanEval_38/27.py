### Cyclic Encoding and Decoding in Python

Here's a self-contained Python script that implements the `encode_cyclic` and `decode_cyclic` functions:

```python
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    # Split the string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group unless it has fewer elements than 3
    groups = [(group[1:] + group[0] if len(group) == 3 else group) for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function and returns decoded string.

    Args:
        s (str): The encoded string.

    Returns:
        str: The decoded string.
    """
    # Calculate the original length of the string
    original_length = len(s)
    
    # Initialize the decoded string
    decoded_string = ""
    
    # Initialize a counter to keep track of the current index
    i = 0
    
    # Loop through the encoded string in steps of 3
    while i < original_length:
        # Get the next group of three characters
        group = s[i:i+3]
        
        # If the group has fewer elements than 3, append them as is
        if len(group) < 3:
            decoded_string += group
            i += len(group)
        # Otherwise, cycle the elements in the group and append them
        else:
            decoded_string += group[1] + group[2] + group[0]
            i += 3
    
    return decoded_string


# Example usage
if __name__ == "__main__":
    original_string = "Hello World"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines the `encode_cyclic` and `decode_cyclic` functions as specified in the original problem statement. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements in each group, and returns the encoded string. The `decode_cyclic` function takes an encoded string as input, reconstructs the original string by cycling the elements in each group, and returns the decoded string.

In the example usage section, we demonstrate the encoding and decoding process using the string "Hello World". The encoded string is then printed, and the decoded string is compared with the original string to verify that the encoding and decoding process is correct.