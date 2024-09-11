### Cyclic Encoding and Decoding in Python

Below is a Python script that includes the `encode_cyclic` and `decode_cyclic` functions.

```python
def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded
    :return: Encoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Input string to be decoded
    :return: Decoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group back to the original order. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example use case:
if __name__ == "__main__":
    input_str = "abcdefgh"
    encoded_str = encode_cyclic(input_str)
    decoded_str = decode_cyclic(encoded_str)
    
    print("Input String:", input_str)
    print("Encoded String:", encoded_str)
    print("Decoded String:", decoded_str)
```

In the `decode_cyclic` function, I have modified the line `groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]` to `groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]` so that each cycle of characters is reversed back to its original order.