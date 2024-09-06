```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python script uses the `hashlib` module to generate an MD5 hash. The `string_to_md5` function takes a string text as input and returns its MD5 hash as a string, or None if the input string is empty. The function uses the `utf-8` encoding to convert the text to a bytes-like object before updating the MD5 hash object with the input data. The resulting hexadecimal hash is then returned as the output. 

To use this script, you can simply call the `string_to_md5` function with the desired input text, as demonstrated in the provided test case. 

You can verify the integrity of the MD5 hash by comparing it to the expected output, as shown in the comment:
```python
>>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
``` 

To further validate the correctness of the script, you may want to consider additional test cases, such as empty input or long strings, to cover different scenarios and ensure consistent behavior.