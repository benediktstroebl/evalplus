Here's a Python script with a self-contained function that solves the problem:
```python
# !pip install codepoints
import string
from codepoints import codepoints

def shift_encoding(string: str):
    base_shift = 5
    alphabet_size = len(string.upper())
    
    def shift_character(char):
        nonlocal base_shift, alphabet_size
        offset = (ord(char) + base_shift) % alphabet_size
        return chr(offset)
    
    shifted = ''.join(map(shift_character, string))
    return shifted

# Example usage
message = "Hello World!"
encoded = shift_encoding(message)
print(encoded)
```

This code defines a function `shift_encoding` that shifts each character of an input string by a specified base shift amount. It ensures that the shifted characters still fall within the ASCII range. The example usage demonstrates how to use this function to encode a message.