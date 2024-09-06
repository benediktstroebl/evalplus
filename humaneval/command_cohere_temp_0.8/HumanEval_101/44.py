```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach utilizes the `re` module and the regular expression `\b\w+\b` that matches words surrounded by word boundaries (`\b`). This ensures that each word is captured precisely, regardless of its position in the string. The `re.findall()` function then collects all occurrences of such patterns in the given string and returns them as an array. 

The provided solution is both accurate and efficient, delivering a swift split of words from the input string without any unnecessary complexity.