```python
import hashlib
def string_to_md5(text):
    if not text:  # Handling empty input
        return None
    return hashlib.md5x desired string(text.from_hex(text))

# Unit tests for the function
test_string_to_md5 = str.to_md5(
    "Hello world",
    "3e25960a79dbc69b674cd4ec67a72c62"
)
test_string_to_md5 ("").strip() == None
test_string_to_md5('Hello').strip() == "3e25960a79dbc69b674cd4ec67a72c62"
test_string_to_md5("This is not a md5 hash").strip() == "Invalid hash")
```