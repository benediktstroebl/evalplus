```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the `re.findall()` function from the `re` module in Python. The regular expression pattern `\w+` matches one or more word characters (letters, digits, and underscores), effectively separating the input string `s` into an array of words. This matches the specification of the task outlined in the original prompt.

The function removes any commas or spaces from the string and returns a list of the words. To achieve this, we use the regular expression `r'\w+'` that matches one or more word characters (which include letters, digits, and underscores). This efficiently splits the input string into an array of words.

To further clarify, the `re.findall()` function finds all occurrences of the pattern in the string, returning them as an array. In this case, each found word becomes an element of the returned list. 

Note: The `re` module is a built-in Python module providing comprehensive support for regular expressions, making it a powerful tool for text processing and analysis. It offers a wide range of functionalities for pattern matching and manipulation of strings based on flexible patterns.