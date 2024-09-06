Here's a Python script with a self-contained function that solves the problem you've outlined, along with a marked section for the code to be copied:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character 5 steps in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if ((ord(ch) - ord("a")) % 26) - 5 > 0 else (((ord(ch) - ord("a")) % 26) - 5)) for ch in s])

# Copy this code block into "encoded_shift.py"
# Use encode_shift function by calling encoded_shift("YOUR STRING HERE")
```

You may use the functions by calling `encode_shift()` with a string to encode it, and `decode_shift()` with the encoded string to decode it. 
The code block above can be copied into a file called `encoded_shift.py` to be used as a module. In order to use the encode_shift function, you must call `encoded_shift("YOUR STRING HERE")` and print the returned value from the console. If no value is returned, the function call will return the encoded string as a result.  You can also decode THAT encoded value using the `decode_shift()` function.

Let me know if I've understood your problem correctly and if this solution suits your needs! Feel free to ask if you have any other questions.