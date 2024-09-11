Here is a self-contained Python script that solves the problem:
```markdown
### Caesar Cipher Encoder and Decoder

#### Problem:
- `encode_shift(s: str):` returns encoded string by shifting every character by 5 in the alphabet.
- `decode_shift(s: str):` takes as input string encoded with `encode_shift` function. Returns decoded string.

#### Solution:

```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.

    :param s: input string
    :return: encoded string
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: input string
    :return: decoded string
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

This script uses the `ord()` function to get the ASCII value of a character and the `chr()` function to get the character represented by a specific ASCII value. The Caesar cipher shift is applied by adding or subtracting the shift value from the ASCII value of the character and taking the modulus with 26 to wrap around the alphabet. The `isalpha()` and `islower()` methods are used to handle both lowercase and uppercase letters. Non-alphabetic characters are left unchanged.