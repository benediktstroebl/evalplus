```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script features a function `string_to_md5` that computes the MD5 hash of a given text string. The MD5 hash is a fixed-length, 32-byte hexadecimal string unique to each input string. The function leverages the `hashlib` module in Python which provides developers with an easy way to calculate message digests and hashes.

This function addresses the issue stated in the prompt. It handles the scenario of an empty input string gracefully by returning `None`. Furthermore, it encodes the input string into bytes to facilitate the hash calculation by the `md5` object from the `hashlib` module, and subsequently returns the hexadecimal representation of the calculated hash value, enabling simple comparison with expected values.

Here's an example of using this function:
```python
md5_result = string_to_md5('Hello world')
print(md5_result)  # Output: 3e25960a79dbc69b674cd4ec67a72c62
```

This would output:
```bash
3e25960a79dbc69b674cd4ec67a72c62
```

If an empty string is passed in, here's how you'd handle it:
```python
md5_result = string_to_md5('')
print(md5_result)  # Output: None
```

The output would be:
```python
None
```