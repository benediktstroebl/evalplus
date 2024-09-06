```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the `re.findall()` method in conjunction with the regular expression pattern `r'\w+'`. This pattern identifies sequences of word characters (punctuation marks are ignored) within the input string, allowing the function to return a list of discrete words from the given input. 

The regular expression pattern `\w+` matches one or more word characters. The word characters commonly include alphabets (both uppercase and lowercase), and underscore (_). 

To retain the punctuations and other special characters, one can simply not include them in the pattern, which would lead to more comprehensive results.