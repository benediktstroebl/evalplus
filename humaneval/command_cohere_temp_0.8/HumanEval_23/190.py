```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script defines a function called `strlen` that takes a string as an argument and returns the length of that string. The function uses the `len()` function, which is a built-in Python function, to determine the number of characters in the given string. 

This function is aptly named according to PEP 8 standards, which suggest that a function should be named using snake_case, meaning that the first word is lowercase and all subsequent words are capitalized without spaces. 

If you would like to test this function, you can call it with a string argument in the same way as the example provided in the original prompt. 
Here is an example of how you can test this function: 
 ```python
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('a_longer_string_with_many_characters')
18
``` 
This would return a result of 0 for an empty string, 3 for the string 'abc', and 18 for the string 'a_longer_string_with_many_characters'.