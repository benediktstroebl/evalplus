```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the powerful `re` module in Python for efficient and effective text processing. The function `re.findall()` searches through the given string `s` for sequential word matches using the regular expression `\w+`, which identifies consecutive sequences of word characters (letters, numerals, and underscores). These word matches are then returned as an array.

The regular expression `\w+` is particularly effective here because it eliminates the need for defining word boundaries with care, as well as any concerns about overlapping matches, which are handled correctly by this expression. This results in a concise and robust solution to the problem.