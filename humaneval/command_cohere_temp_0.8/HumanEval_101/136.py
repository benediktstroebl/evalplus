```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the powerful `re` module in Python for regular expressions. The function `re.findall()` searches the given string `s` for all occurrences of the pattern `\w+`, which matches one or more word characters (letters, digits, and underscores). These matches are returned as an array. 

The regular expression pattern `\w+` is crafted to efficiently capture discrete words from the input string, regardless of whether the words are separated by commas or spaces. This method offers a concise solution to the problem, showcasing the efficacy of regular expressions for string manipulation. 

The `re` module is concurrently executing several optimizations to ensure that the matching process is performed effectively. This inherent efficiency provides faster performance for various use cases, making it a valuable tool within the Python ecosystem. 

This approach provides a straightforward, efficient solution to the problem, demonstrating the utility of Python's `re` module for word extraction from strings.