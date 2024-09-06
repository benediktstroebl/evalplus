```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the `re.findall()` function from the `re` module in Python. The regular expression pattern `\w+` matches one or more word characters (letters, digits, and underscores), effectively splitting the input string `s` into an array of words. This function returns the list of words from the given string.

To adhere to the specified problem guidelines, this solution assumes that commas and spaces are the only separators between words in the input string. If the input might contain different or more complex separators, the function might need to include additional logic for handling those cases.