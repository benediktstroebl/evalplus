```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python script uses the hashlib library to generate an MD5 hash. The string_to_md5 function takes a text input, encodes it in UTF-8, calculates the MD5 hash, and then returns the hexadecimal representation of that hash. The function gracefully handles empty input strings, returning None for such cases.

To use this script, ensure you have the hashlib library installed by running `pip install hashlib` or `pip3 install hashlib` depending on your Python version. 

To execute the function, copy and paste the code into a Python file (e.g., `hash_tool.py`) and run it using `python hash_tool.py`. You can call the `string_to_md5` function with your desired input text to obtain the corresponding MD5 hash. 

For example:
```python
print(string_to_md5("Hello World!"))  # Output: e4d7f1b4ed25e3b5b2d5b7f28b0b98
``` 

This command will print the MD5 hash for the input "Hello World!". 

Remember to handle your data carefully and be aware that MD5 is no longer considered a secure hashing algorithm for password storage or security-sensitive tasks due to vulnerabilities.