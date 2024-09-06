```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string,
    or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to compute the MD5 hash of the input `text`. It checks if the input is empty or contains only whitespace by using the `strip` method before deciding to return the hash or `None`. This method ensures that empty strings are handled correctly, as per the problem statement. The function is also annotated with type hints to indicate that it accepts a string input and returns either a string or `None` accordingly.

To use this function in the context of the given problem statement, you can execute it with specific inputs and verify the results against the expected MD5 hashes, as shown in the provided comment.