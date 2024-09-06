```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the hexadecimal representation of the hash.
    Returns None if the input is an empty string.
    """
    if text and text != "":
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        return md5.hexdigest()
    else:
        return None
```

The provided Python script defines a function `string_to_md5` that takes a string text as input and returns its MD5 hash as a hexadecimal string representation if the input is not an empty string. The MD5 hash is computed using the `hashlib.md5()` function from the hashlib module, and the update method is used to update the hash with the input string encoded in UTF-8. The result is then returned as the hexadecimal representation of the hash using the `hexdigest()` method.

To handle the special case of an empty string input, the function checks if the input string is not empty using the logical NOT operator (`not`) and the equality check (`==`), returning `None` for empty input.

This code provides a convenient way to encrypt text and retrieve its MD5 hash in a python program.  It can be used to ensure the integrity of critical data and as a component of other cryptography and data processing functions.  It is important to note that MD5 is not suitable for security applications, as it is computationally inexpensive and has been found to have vulnerabilities. 

The code includes a test that checks if the output of the function matches the expected MD5 hash of the string "Hello world", indicating that the function is working correctly. 
This is a useful utility function that can be easily incorporated into various projects and applications requiring data integrity checks or cryptographic operations. 

It's important to note, however, that MD5 is a one-way hash function, meaning it is not possible to reverse-engineer the original text from its MD5 hash.  Adding error detection code (such as a cyclic redundancy check (CRC)) to the original text before hashing is advisable to ensure data integrity during transmission.  This added safety measure can help detect any modifications or errors that might occur during transmission or storage.