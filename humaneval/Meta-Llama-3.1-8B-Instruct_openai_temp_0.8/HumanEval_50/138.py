```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes all characters in the string are lowercase letters.
    
    :param s: The string to be encoded
    :return: The encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes all characters in the string are encoded lowercase letters.
    
    :param s: The encoded string
    :return: The decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage:
if __name__ == "__main__":
    input_str = "hello"
    encoded_str = encode_shift(input_str)
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

Please note that the `ord` function returns the ASCII value of a character, and subtracting `ord("a")` will shift the ASCII values to start from 0 for 'a'. The modulo operation by 26 ensures that the shifted value stays within the range of lowercase letters. The `chr` function is used to convert the shifted ASCII values back to their corresponding characters. 

Also note that the above code does not handle cases where the input string contains characters other than lowercase letters. You might want to add error handling for such cases, depending on your requirements. 

For example, you could modify the functions to return an error message when encountering non-alphabetical characters:

```python
def encode_shift(s: str):
    result = []
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                result.append(chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")))
            else:
                result.append(chr(((ord(ch) - ord("A") + 5) % 26) + ord("A")))
        else:
            result.append(ch)
    return "".join(result)


def decode_shift(s: str):
    result = []
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                result.append(chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")))
            else:
                result.append(chr(((ord(ch) - ord("A") - 5) % 26) + ord("A")))
        else:
            result.append(ch)
    return "".join(result)
```