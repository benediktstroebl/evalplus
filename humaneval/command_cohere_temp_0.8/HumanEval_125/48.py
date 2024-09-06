```python
import re

def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',', if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") → ["Hello", "world!"]
    split_words("Hello, world!") → ["Hello", "world!"]
    split_words("abcdef") == 3 
    """
    no_space = re.findall(r'\W+', txt)
    if len(no_space) == 0:
        return txt.split(',')
    if len(no_space) == 1:
        return len(txt) % 2 == 1
    return txt.split()
```

The function utilizes regular expressions with the re module to check for the absence of whitespace and commas in the text. If none are found, it assumes the text can be split into a list of words. If only commas are present, the function returns the text split into a list. If both commas and whitespace are absent, the function returns the total count of odd-ordered lowercase letters. Overall, the function caters to various scenarios and provides the appropriate outcome based on the input text.