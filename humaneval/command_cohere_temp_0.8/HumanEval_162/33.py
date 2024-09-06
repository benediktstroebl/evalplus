```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text and text.strip():
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to generate an MD5 hash. It validates the input as either a blank string or none and then encodes the text before creating the hash object. The function returns the hexadecimal representation of the hash, or None if the input is invalid. 

To ensure accuracy, remember to install the `hashlib` library, which is a standard Python library so it can be pip installed `pip install hashlib` and imported into your script. 

The test case provided in the problem statement can be replaced with a more comprehensive test strategy to cover edge cases and verify the function's correctness thoroughly. 

Let me know if you would like to discuss test strategy or any further questions you may have!