```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python script uses the `hashlib` module to generate an MD5 hash. The `string_to_md5` function takes a string text as an argument and returns its MD5 hash as a string, or None if the input is an empty string. 

The MD5 hash algorithm is a cryptographic protocol that hashing into a 128-bit hash value, which is a 32-digit hexadecimal number. It is designed to be a very fast algorithm that can securely hash data with a low risk of collision. 

It is important to note that the MD5 hash function has vulnerabilities and is not considered secure for certain applications. However, it is still widely used for non-security critical tasks, such as data integrity checks. 

To ensure that the function behaves correctly in all cases, we include a test case in the script that verifies the behavior of `string_to_md5` with an example input. The test case checks if the MD5 hash of the string "Hello world" is equal to the expected hash "3e25960a79dbc69b674cd4ec67a72c62". The MD5 hash function is deterministic, so this expected hash value can be confidently precomputed and hard-coded into the test case. 

To execute this test case, you can call the function with the corresponding input and verify if the returned value matches the predetermined hash value. 

```python
string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
``` 
The output of running this code will be `True`, as the MD5 hash for the string "Hello world" is "3e25960a79dbc69b674cd4ec67a72c62". 

If you modify the example input and provide a different string, the function will return the corresponding MD5 hash of this modified string, which could be different from the precomputed hash value in the test case. 

Also, if you input an empty string, the function will return `None` accordingly. 

This test case is a good starting point, but to ensure the function is robust, it is important to consider adding more test cases to cover various scenarios and edge cases, including multi-byte characters, uppercase letters, special symbols, and more.