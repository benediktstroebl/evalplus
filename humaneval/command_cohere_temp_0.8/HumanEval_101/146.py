```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the `re.findall` method in conjunction with the regular expression pattern `\w+` to extract all the words from the given string. The pattern `\w+` matches one or more alphanumeric characters, giving us the desired array of words.