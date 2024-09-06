```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It first checks if the `text` argument is provided, and if it's not empty or containing only whitespace characters through the `strip()` method. If the condition is met, the function uses the `hashlib.md5()` method to calculate the hash of the text string, which is then returned as a hexadecimal string using `hexdigest()`. If the input is empty or contains only whitespace, the function returns `None`. 

This MD5 hash function provides a unique fingerprint for text data, and it's widely used in cybersecurity and data integrity applications. 

You can verify the correct functionality of the function by using the test case provided in the problem statement prompt. 
Here is an example of usage:
```python
>>> string_to_md5('Hello world')
'3e25960a79dbc69b674cd4ec67a72c62'

>>> string_to_md5('')
None
``` 

This demonstrates the function's behavior, showcasing how it handles different scenarios.