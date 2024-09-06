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
    if no_space:
        return txt.split(',')
    no_comma = re.findall(r'\w+,\w+', txt)
    if no_comma:
        return [txt]
    else:
        return len(re.findall(r'([a-z])([a-z]*)', txt)) % 2
```

The script utilizes regular expressions and string methods to achieve the needed functionality.

The `re.findall` function is used to identify patterns in the string that indicate the presence of word separation:
- `\W+` targets consecutive sequences of non-word characters (eg. punctuation).
- `\w+,\w+` targets words separated by a comma.

If neither whitespace nor commas are present, the function returns the number of letters with odd alphabetical order. This is calculated by using `re.findall` to find all single letters and then counting the odd ones.