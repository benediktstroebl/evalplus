Here's a Python script that solves the problem:

```markdown
### Caesar Cipher Encoding and Decoding

#### Problem Description

This script implements a Caesar cipher encoder and decoder.

#### Code

```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Input encoded string to be decoded
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Test the functions
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

#### Explanation

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input, shifts each letter by 5 places in the alphabet, and returns the encoded string. The `decode_shift` function takes an encoded string as input, shifts each letter back by 5 places in the alphabet, and returns the decoded string.

The functions use the ASCII values of the characters to perform the shift operations. The `ord` function returns the ASCII value of a character, and the `chr` function returns the character represented by a specific ASCII value.

The script also includes a test case to demonstrate the usage of the functions. The original string "Hello, World!" is encoded using `encode_shift`, and then decoded using `decode_shift`. The original, encoded, and decoded strings are printed to the console.

Note that this script only shifts letters and leaves other characters (such as spaces, punctuation, and digits) unchanged. Additionally, the script converts the input string to lowercase before encoding and decoding to ensure consistent behavior.