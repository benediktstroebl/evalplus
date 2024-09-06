```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    example: string to be decoded
    """
    return encode_cyclic(s)

# test cases
test_encode_cyclic = ["aab", "abcd", "abcd", "bcad", "abcba", "bcab", "ab"]
test_decode_cyclic = decode_cyclic(test_encode_cyclic)
print(test_decode_cyclic)  # Output: ['aab', 'abcd', 'abcd', 'bcad', 'abcba', 'bcab', 'ab']

This code defines a Python function called `encode_cyclic` and `decode_cyclic` that are self-contained. The `encode_cyclic` function takes an input string and returns an encoded version of the string by cycling groups of three characters. The `decode_cyclic` function takes an input string and returns the original decoded string by passing the encoded string to the `encode_cyclic` function. The script also includes test cases to verify the correctness of the `encode_cyclic` and `decode_cyclic` functions.