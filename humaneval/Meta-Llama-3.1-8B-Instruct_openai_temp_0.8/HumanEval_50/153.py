```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every lowercase character by 5 in the alphabet.
    
    Parameters:
    s (str): the input string to be encoded.
    
    Returns:
    str: the encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): the input string to be decoded.
    
    Returns:
    str: the decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else ch for ch in s])


# Example usage
if __name__ == "__main__":
    original_str = "hello world"
    encoded_str = encode_shift(original_str)
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

In this code, the `encode_shift` function shifts every lowercase alphabetic character in the input string by 5 positions in the alphabet. The `decode_shift` function reverses this process to decode the string. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `% 26` operation is used to wrap around the alphabet in case of characters that are shifted beyond 'z'. The `isalpha` and `islower` methods are used to check if a character is alphabetic and lowercase, respectively. Non-alphabetic characters are left unchanged.