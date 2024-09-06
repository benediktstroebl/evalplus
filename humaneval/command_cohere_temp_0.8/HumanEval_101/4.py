```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach leverages the power of regular expressions to effectively split the input string into words using the `re.findall()` function. The regular expression pattern `\w+` matches one or more word characters (letters, digits, and underscores), effectively isolating each word in the given string.

To handle various separators (commas and spaces) between words, the `re.findall()` function is used, which returns all non-overlapping occurrences of the pattern in the string. This means that regardless of whether the words are separated by commas or spaces, the function will still provide the correct list of words.