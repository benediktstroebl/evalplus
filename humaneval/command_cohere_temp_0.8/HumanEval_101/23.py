Here's a Python script that contains a function called `words_string` which takes a string as an input and returns a list of words separated by commas or spaces:
```python
def words_string(s):
    return s.split()
```

The `words_string` function utilizes the `split()` method, which examines the string `s` for occurrences of whitespace. It then divides the string into a list of words, excluding any empty strings that may occur during the splitting process, thereby resulting in a list of words. This list is then returned. 

This approach is not case-sensitive, meaning that it will treat 'Hi' and 'hi' as the same word. If you would like to distinguish between capitalized and lowercase words, you may want to include a normalization step or consider using a different method for splitting the string. 

This approach also assumes that words contain text only and do not include any special characters or punctuation marks. If your words include these, you may want to include an additional step to handle these special cases.