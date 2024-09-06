```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text.strip() == "":
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function `string_to_md5` that takes a text string as input. If the input is an empty string, the function returns `None`. Otherwise, it utilizes the `hashlib` module to calculate the MD5 hash of the input text and then returns the hexadecimal representation of this hash.

The MD5 hash is considered a cryptographic hash function that takes a large input and generates a fixed-size, 128-bit hash value. Although MD5 was initially designed as a cryptographic hash function, it has since been found to have vulnerabilities, which is why it is no longer recommended for secure applications. Nevertheless, it remains a popular tool for checking data integrity, comparing files, and generating unique identifiers for files and strings. 

In the context of the function provided, it can be used to efficiently determine if two strings are equal by comparing their MD5 hashes, which significantly reduces the complexity compared to a direct string comparison. The function incorporates a UTF-8 encoding prior to the hash calculation to ensure that all kinds of Unicode characters are correctly processed. 

To test the correctness of the function, you can compare the output of `string_to_md5("Hello world")` with the expected MD5 hash of "3e25960a79dbc69b674cd4ec67a72c62". 

It's important to note, however, that MD5 is not suitable for secure cryptographic applications due to its vulnerabilities. This script is primarily intended for demonstrating the implementation of MD5 hash calculation in Python and solving the specified problem, not for secure hash function usage. 

In summary, the script provides a functional solution to the problem with a straightforward Python implementation. 
            
         ```