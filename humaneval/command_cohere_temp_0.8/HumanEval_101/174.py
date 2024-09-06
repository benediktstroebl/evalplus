```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach leverages the power of regular expressions to efficiently split the string into words while accounting for variations in spacing, thereby achieving the desired result as specified in the prompt.

The function `re.findall()` is used to find all occurrences of words amidst the commas and spaces within the given string `s`. The regular expression `r'\b\w+\b'` helps in capturing whole words. The circumflex `^` signifies the start of a line, and the `\b` characters form word boundaries, ensuring accurate separation of words even in the presence of commas and spaces.