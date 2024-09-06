```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function uses the hashlib library in Python to calculate the MD5 hash of the input text. The function encodes the text in UTF-8 format before calculating the hash to ensure compatibility with the hash function. The result is then converted to a hexadecimal string using the hexdigest() method of the MD5 object.

If the input is an empty string, the function returns None instead of the MD5 hash of the empty string, as per the problem statement. 

To use this function in your code, you can simply import it and call it with your desired input text:
```python
import string_to_md5

result = string_to_md5.string_to_md5('Hello world')
print(result)  # Output: 3e25960a79dbc69b674cd4ec67a72c62
``` 
This would output the MD5 hash of the string "Hello world", which is "3e25960a79dbc69b674cd4ec67a72c62". 

If you pass an empty string, the function will return None:
```python
result = string_to_md5.string_to_md5('')
print(result)  # Output: None
``` 
If you want to ensure the output is a string instead of None when an empty string is given, you can wrap the return in a conditional:
```python
def string_to_md5(text: str) -> str:
    if not text:
        return "Empty String"
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```
In this version, if the input is an empty string, the function will return the string "Empty String".