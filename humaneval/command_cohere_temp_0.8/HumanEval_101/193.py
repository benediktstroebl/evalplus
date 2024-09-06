```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the powerful `re` module in Python for efficient pattern matching and word extraction. The regular expression pattern `\w+` matches one or more word characters (letters, digits, and underscores), effectively separating the input string into an array of words.

The function then uses the `re.findall()` function to find all occurrences of the pattern in the input string and returns them as an array. This method is not only effective and concise but also efficiently handles various input scenarios, including spaces, commas, and different word types, ensuring correct word separation.