```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function `string_to_md5` that computes the MD5 hash of a given string `text`. The function employs the `hashlib` module to generate the hash, and the `update` method to feed the string into the hash function. The result is returned as a hexadecimal string using the `hexdigest` method. Importantly, the function returns `None` if the input string is empty, in compliance with the problem's request. This null return ensures that the function handles empty inputs gracefully.

Here is an illustrative example of how to use the `string_to_md5` function:
```python
# Example usage
md5_hash = string_to_md5('Hello World')
print(md5_hash)  # Output: 3e25960a79dbc69b674cd4ec67a72c62

md5_hash = string_to_md5('')
print(md5_hash)  # Output: None
```

In the first example, the MD5 hash for the string "Hello World" is calculated and printed, yielding the expected output of "3e25960a79dbc69b674cd4ec67a72c62". In the second example, the function efficiently handles the empty string, returning `None`, as promised by the problem's specification. This showcases the function's ability to handle varying scenarios gracefully. 

Note: The MD5 hash, a ubiquitous message-digest algorithm, hashing security properties. It is typically employed to verify data integrity, with its simple design making it ideal for fast recognition. However, MD5 is no longer recommended for cryptographic purposes due to vulnerabilities like collisions. For more information, consult a cryptography guide.