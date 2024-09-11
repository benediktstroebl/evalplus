```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by converting each character to its ASCII value, adding 5 if it's a lowercase letter, and then taking the modulus with 26 to wrap around the alphabet.
    
    Parameters:
    s (str): The input string to encode.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works by shifting every character back by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to decode.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5 + 26) % 26 + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


# Test the functions
print(encode_shift("hello"))  # Output: "mjqqt"
print(decode_shift("mjqqt"))  # Output: "hello"
```

This script defines two functions, `encode_shift` and `decode_shift`, which implement the Caesar cipher with a shift of 5. The `encode_shift` function shifts each lowercase letter in the input string by 5 positions, and the `decode_shift` function does the opposite. The functions use the ASCII values of characters to perform the shift, and the `isalpha` and `islower` methods of strings to check if a character is a letter and if it's lowercase, respectively. The `% 26` operation is used to wrap around the alphabet.