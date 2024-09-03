```python
import hashlib
def string_to_md5(text):
    if not text:  # empty string returns None
        return None
    return hashlib.md5arenum(text)

# tests
md5_hash = string_to_md5("Hello world")
print("md5_hash =", md5_hash)  # should print "md5_hash = '3e25960a79dbc69b674cd4ec67a72c62'"

md5_hash = string_to_md5("")
print("md5_hash =", md5_hash)  # should print "md5_hash = None"

# Test empty string
md5_hash = string_to_md5("")
print("md5_hash =", md5_hash)  # should print "md5_hash = None"

# Test non empty string
md5_hash = string_to_md5("abc")
print("md5_hash =", md5_hash)  # should print "md5_hash = 'abc'a5fshell'"
```
The script defines a function `string_to_md5` that converts a given text to its MD5 hash. It then tests the common use cases, an empty string returns `None`, and a non-empty string returns the corresponding MD5 hash. The tests are designed to ensure the correctness of the function's behavior.