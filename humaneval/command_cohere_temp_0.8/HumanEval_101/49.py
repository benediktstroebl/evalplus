Here's a Python script that contains a function `words_string` that splits a string into an array of words given a string that contains a space or comma separated list of words:
```python
def words_string(s):
    return s.split(', ')
```
The function uses the `split` method in Python which can receive more than one character as a parameter to split the string, in this case, we are using commas and spaces to correctly split the string into words.

This solution is straightforward and effectively splits the input string into words.