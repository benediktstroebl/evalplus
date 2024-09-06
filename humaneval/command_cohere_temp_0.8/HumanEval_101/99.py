```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach leverages regular expressions to split the string into words using the `re.findall()` function. The regular expression `\b\w+\b` ensures that only words are captured, eliminating any punctuation marks or special characters. This is particularly useful when the input string may contain various types of data, including emails, names, and messages.

The function accepts a string as input and returns a list of words found in the string, ensuring compatibility with the specified problem statement. This solution provides a clean and efficient way to manage strings and achieve the desired outcome of separating words.