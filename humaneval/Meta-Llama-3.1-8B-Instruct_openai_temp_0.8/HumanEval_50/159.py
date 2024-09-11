```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    :param s: Input string to be decoded
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

In this code:

- We use the `ord` function to get the ASCII value of a character and `chr` function to get the character represented by a specific ASCII value.
- We subtract the ASCII value of 'a' to shift the range from ASCII values of 'a' to 'z' to a range from 0 to 25.
- We use the modulo operator (`%`) to ensure the shifted value stays within the range 0-25.
- We add the ASCII value of 'a' back to get the ASCII value of the shifted character.
- We convert the input string to lowercase to simplify the calculation and handle both lowercase and uppercase letters.
- We use the `isalpha` method to check if a character is a letter, and only shift letters.
- The example usage demonstrates how to use the `encode_shift` and `decode_shift` functions.