```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the `re.findall()` function from the `re` module in Python. The regular expression pattern `\w+` matches one or more word characters (letters, digits, and underscores). This effectively isolates each word within the provided string `s`, regardless of whether the words are separated by commas or spaces.

The function returns a list of strings, each of which represents a word from the input string. Thus, it successfully solves the problem as stated in the given prompt.

The provided solution offers a concise and efficient way to parse strings of words into individual elements, making it a robust tool for word-related operations in various coding tasks.