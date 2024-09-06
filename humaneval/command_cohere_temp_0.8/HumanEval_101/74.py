```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes regular expressions with the `re.findall()` function to efficiently split the string into words based on one or more alphanumeric characters (`\w+`). This ensures that each word is captured, even if there are multiple spaces between them.

The regular expression pattern (`\w+`) matches one or more of the following characters:
- Latin letters (upper and lowercase)
- Arabic numerals
- underscore (_)
- Asterisk (*)

This pattern allows the function to handle various input scenarios, such as different types of spaces, capitalization, and special characters, providing the expected output for the given problem.