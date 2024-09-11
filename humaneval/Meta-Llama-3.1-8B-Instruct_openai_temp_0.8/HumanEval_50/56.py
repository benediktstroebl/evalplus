### Shift Encoder and Decoder

Below is a Python script that implements the `encode_shift` and `decode_shift` functions as described, along with a third function `decode_shift` to reverse the encoding process.

```markdown
### shift_encoder.py

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by incrementing the ASCII value of each character by 5,
    then wrapping around to the beginning of the alphabet if necessary.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by subtracting 5 from the ASCII value of each character,
    then wrapping around to the end of the alphabet if necessary.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage
if __name__ == "__main__":
    input_string = "hello123"
    encoded_string = encode_shift(input_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

### Running the Script

You can run the script by saving it to a file named `shift_encoder.py` and executing it with Python:

```bash
$ python shift_encoder.py
```

This will encode the input string `"hello123"` and then decode the result to demonstrate the functionality of the `encode_shift` and `decode_shift` functions.