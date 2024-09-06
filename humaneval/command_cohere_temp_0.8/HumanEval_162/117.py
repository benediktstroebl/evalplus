```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function called `string_to_md5` that takes a string text as input. Within the function, it checks if the input text is empty using the condition `if not text:`. If the text is empty, the function returns `None`, indicating that the input string produced an invalid MD5 hash. Otherwise, it proceeds to compute the MD5 hash of the input text. 

To do this, it uses the `hashlib` module to create an instance of the MD5 hash algorithm, stored in the `md5` variable, which is then used to update the hash with the utf-8 encoded version of the input text using the `update()` method. This produces a unique hash value for the input string. 

Finally, the function returns the hexadecimal representation of the MD5 hash using the `hexdigest()` method on the `md5` object. 

The purpose of the script is to provide a self-contained solution for converting any given string into its MD5 hash, whilst also handling empty strings correctly, and adheres to the problem statement provided. It is important to note that MD5 hashes are no longer considered secure and have vulnerabilities making them unsuitable for certain security-related purposes. However, the script still serves to effectively solve the problem as described. 

To verify the correctness of the script, you can compare its output with the provided test case: `string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'`.