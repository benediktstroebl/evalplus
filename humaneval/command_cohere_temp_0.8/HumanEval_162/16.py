```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function leverages the hashlib module to compute the MD5 hash of a given text string. It employs the encode method to convert the text into a binary-compatible format before calculating the hash using the md5 function from the hashlib module. The resulting hash is then distilled into a hexadecimal string using the hexdigest method. 

The function is carefully crafted to return None when the input text is empty or contains only whitespace, ensuring consistent behavior. This null return is a prudent choice to handle vacant input strings, preventing the occurrence of errors or unexpected outcomes. 

To demonstrate the function's behavior, we can use a test string, compare the result with the expected MD5 hash, and confirm their equality. The function stands ready to tackle real-world scenarios effectively and ensures data integrity with its dependable hash computation. 

This function exhibits the dependability of Python in securely handling hash calculations and maintaining robustness through thoughtful handling of empty inputs.