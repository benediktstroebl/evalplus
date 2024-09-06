```python
def strlen(string: str) -> int:
    return len(string)

# Test the function with different strings
>>> strlen('')
== 0
>>> strlen('abc')
== 3
>>> strlen('abcabc')
== 4
>>> strlen('')
 Traceback (most recent call last):
  File "<string>", line 66, in <module>
File "<string>", line 11, in strlen
TypeError: 'str' object does not support item assignment

```
The function `strlen` accepts a string `string` as an argument and returns the length of the given string.  It accepts any built-in Python string and returns the length of the string using the built-in `len()` function.