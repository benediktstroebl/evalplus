```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach leverages regular expressions to match individual words using the `\b` delimiter, which represents a word boundary, and the `\w+` pattern matches one or more word characters. The `re.findall()` function then returns all occurrences of this pattern in the input string as an array. 

To use this code, you'll need to install the `re` module:
```bash
pip install re
```

The script adheres to the problem statement, providing a standalone Python function that splits a given string into words and returns an array of those words. It does not rely on any external dependencies other than the `re` module, which is necessary for the regular expression functionality.