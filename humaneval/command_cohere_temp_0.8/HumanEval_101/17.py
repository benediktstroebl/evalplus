```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach leverages the power of regular expressions, specifically the word matching `\w+` expression, to cleanly split the string into individual words. This ensures consistency in handling various scenarios of string inputs with commas and spaces. The function then uses the `re.findall()` function to find all occurrences of words and returns them as an array.