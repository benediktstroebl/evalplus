```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.
    
    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it's not empty, otherwise None.
    """
    if text:
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
    else:
        return None
```

The provided Python function string_to_md5 takes a text string as input and returns its MD5 hash as a hexadecimal string, following the convention of returning None for empty input strings to handle them gracefully. This MD5 hash is a unique "fingerprint" for the input string, computed using a cryptographic hash function. The hashlib module in Python provides a convenient way to perform this hash calculation. 

The function starts by creating an instance of the MD5 hash object using hashlib.md5(), encoding the input string text first to accommodate byte-like input expected by the hashlib module. 

The .hexdigest() method on the hash object then returns the hexadecimal representation of the hash value, which is a 32-character string. 

Here's an example of how you might use this function, and what you could expect to see as output:
```python
# Example usage:
print(string_to_md5("Hello World!"))  # This should print a 32-character string
print(string_to_md5(""))  # This should print None
```

This function is versatile and can be used anytime a cryptographic hash is needed, or if you wish to validate that a given string is not empty. 

Note that MD5 is not considered a secure cryptographic hash function nowadays, due to vulnerabilities found over the years. It is therefore not suitable for security-sensitive applications. However, for generic use cases where security is not a concern, MD5 remains a useful and efficient way to perform hash calculations.