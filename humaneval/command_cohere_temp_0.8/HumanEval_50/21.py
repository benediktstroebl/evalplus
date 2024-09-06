Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the code and how to use it:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting every character by 5 in the alphabet.
    
    Args:
        s (str): Input string to be encoded.
    
    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): Input string to encode.
    
    Returns:
        str: Decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) % 26 >= 0 else ((ord(ch) - ord("a")) % 26 + 26)) or ord("a")) for ch in s])

# Test scenarios
def test_encode_shift():
    assert encode_shift("Hello World!") == "Ifmmp Ltd!"
    assert encode_shift("!?@#$%^&*()_+-=[]{}|;:,.<>?") == "rkjhznr brkmizx!"

def test_decode_shift():
    assert decode_shift("Ifmmp Ltd!") == "Hello World!"
    assert decode_shift("rkjhznr brkmizx!") == "!?@#$%^&*()_+-=[]{}|;:,.<>?"

test_encode_shift()
test_decode_shift()
```
To use the functions, simply call them with the appropriate input strings as shown in the tests. 
The `encode_shift` function shifts each character of the input string by 5 in the alphabet, while the `decode_shift` function reverses the encoding process to decode the string. 
The tests will verify that the output of each function is correct. 
Feel free to modify the script to include more tests or add additional functionality as needed. GAAp