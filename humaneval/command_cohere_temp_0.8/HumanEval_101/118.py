```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach utilizes the `re` module and the regular expression `\b\w+\b` which effectively matches individual words with added flexibility to capture special characters, numerals, and underscores, thus ensuring accurate word splitting irrespective of the word composition.

The resulting function is both efficient and robust, making it a reliable solution for the problem at hand.