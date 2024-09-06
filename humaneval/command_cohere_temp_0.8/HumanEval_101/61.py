```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach leverages regular expressions to match individual words using the `\b` delimiter, which represents a word boundary, and the `\w+` pattern captures one or more word characters. The `re.findall()` function then returns all occurrences of this pattern in the input string as an array. 

To use this code, you'll need to install the `re` module, which is part of the standard library in Python, so you can execute the following command in your terminal:
```bash
pip install re
```

This will install the `re` module, which is necessary for utilizing regular expressions in Python. 

Thus, the `words_string()` function can be used to efficiently split a string of words separated by commas or spaces into an array of individual words.