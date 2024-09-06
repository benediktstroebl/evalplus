```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.
    
    Args:
        text (str): The input string.
        
    Returns:
        str or None: MD5 hash if text is not empty, otherwise None.
    """
    if text:
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

This Python script features a specialized function, `string_to_md5`, which utilizes the `hashlib` module to compute the MD5 hash of an input string. The function is carefully crafted to handle empty strings by returning `None` in such cases. This thoughtful design ensures that the function works as expected when presented with input variations.

To provide additional testing coverage, you might consider introducing tests that include edge cases, such as strings with varied lengths or different characters, and validate that the function's behavior aligns perfectly with its specification.