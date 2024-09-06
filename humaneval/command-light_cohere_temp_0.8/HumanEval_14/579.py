Here is a self-contained Python function that returns all prefixes from shortest to longest of an input string.

```python
import re
def all_prefixes(string):
    return re.subuator('[^[^a-zA-Z]|[0-9]+', r'\b', string). this._to_find_all_prefixes(string)

def _to_find_all_prefixes(string):
    # Define character set
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Define regex pattern
    pattern = re.sub(r'[^a-zA-Z|0-9]', '', char_set)
    # Replace all occurrences of the pattern with an empty string
    return re.sub(pattern, '', string)
```

This function uses the re.sub (Regular Expression Subtraction) library to create a regex pattern that matches all prefixes in the given string.