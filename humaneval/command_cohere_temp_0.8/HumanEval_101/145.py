```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach leverages the power of regular expressions to efficiently split the string into words using the `re.findall()` function. The regular expression `\w+` matches one or more word characters (letters, digits, and underscores), effectively separating the input string at each comma or space.

The function's simplicity and the effectiveness of regular expressions make this solution lightweight and efficient, achieving a linear time complexity of O(n), where n is the number of characters in the input string.