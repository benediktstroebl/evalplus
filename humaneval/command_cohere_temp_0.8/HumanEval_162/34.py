```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text.strip() == "":
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

```
The `string_to_md5` function hashes the input text using the MD5 algorithm, ensuring the result conforms to the MD5 hash standard representation as a 32-byte hexadecimal string. It returns `None` for an empty input to conform to the problem's requirement. This function efficiently computes the MD5 hash, which is a one-way cryptographic function that effectively secures data integrity.