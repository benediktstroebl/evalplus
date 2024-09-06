```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the `re.findall()` method in combination with the regular expression pattern `\w+` to extract all the words from the given string. The pattern `\w+` matches one or more word characters, which include all alphanumeric characters and underscores, effectively separating the string into an array of words.