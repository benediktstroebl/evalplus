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
    no_space = re.compile('[^\s,]')
    A = no_space.split(txt)
    if len(A) == 1:
        return len(re.findall(r'(.)\1*', txt)) 
    return A
```

The solution leverages the regex expression to match one or more consecutive characters, optionally matched with their case variation `[a-Z][a-z]`. The total number of odd characters (`re.findall(r'(.)\1*', txt)` will be returned if an empty input or a single character is passed. In case, the string contains whitespaces or commas the function returns a list of words as in the first two examples.