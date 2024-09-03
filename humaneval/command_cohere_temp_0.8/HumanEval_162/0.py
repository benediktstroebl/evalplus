```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function `string_to_md5` that takes a string text as input. It employs the `hashlib` module to calculate the MD5 hash of the input text. The MD5 hash is a unique fingerprint for the input string. The function first checks if the input text is empty. If empty, it returns `None` because an MD5 hash cannot be calculated from an empty string. If the input text is not empty, the function computes the MD5 hash by encoding the text in UTF-8 format and updating the MD5 hash object with the encoded data. Finally, the function returns the hexadecimal representation of the calculated MD5 hash. 

The MD5 hash algorithm has been criticized for its vulnerabilities, namely collision and security issues, which have led to its deprecation in many current cryptographic practices. Despite its shortcomings, the problem statement aims to address practical scenarios where MD5 hashes are still utilized, such as checksum verifications or data integrity checks.

The tests for this function can be exercised by checking the equivalence of the function's output against known MD5 hashes for specific strings. An example test case can be seen in the initial markdown code block provided.