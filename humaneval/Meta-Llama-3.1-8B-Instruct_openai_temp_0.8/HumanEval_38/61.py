### Cyclic Encoding and Decoding
#### Overview

The following Python script provides two functions for encoding and decoding a string using a cyclic pattern.

#### Code
```markdown
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Uncycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "HelloWorld"
    encoded_string = encode_cyclic(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

#### Explanation

The provided code consists of two functions:

- `encode_cyclic(s: str)`: This function takes an input string `s` and encodes it by cycling groups of three characters. It splits the input string into groups of length 3 and then cycles the elements within each group, preserving the original characters in the first and last positions.

- `decode_cyclic(s: str)`: This function takes an input string `s`, which has been encoded using the `encode_cyclic` function, and decodes it back to the original string. It splits the input string into groups of length 3 and then uncycles the elements within each group, effectively reversing the encoding process.

The example usage demonstrates how to use these functions with a sample string and print the original, encoded, and decoded strings for comparison.

Note that the `decode_cyclic` function assumes that the input string was encoded using the `encode_cyclic` function. If the input string has been encoded using a different process, it may not be correctly decoded by this function.