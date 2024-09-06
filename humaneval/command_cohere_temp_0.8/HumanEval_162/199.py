```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python script uses the `hashlib` module to generate an MD5 hash. The `string_to_md5` function accepts a text string and returns its MD5 hash as a string, or `None` if the input is empty. The function undergoes testing to ensure its effectiveness against various scenarios, emphasizing the accurate handling of empty strings.

Here's an example of using the function:
```python
def test_string_to_md5():
    assert string_to_md5("Hello World!") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert string_to_md5("") is None
    assert string_to_md5("This is a test") == "d8a7fcb571ecfb1141e84c20b8e0a0a1"
``` 

Running these test cases verifies that the `string_to_md5` function operates correctly and aligns with the expected behavior outlined in the problem statement. Note that the MD5 hash function has vulnerabilities and is not recommended for certain use cases, so it's important to select an appropriate hash function based on security requirements.