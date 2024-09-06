```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach leverages the power of regular expressions to split the string into words. The `re.findall()` function searches for all occurrences of the regular expression pattern `\b\w+\b`, which matches individual words. The `\b` represents a word boundary, ensuring that only complete words are captured, and `\w+` captures one or more word characters (letters, digits, or underscores). The resulting list of matched words is then returned as the output.

This approach provides a concise solution that delivers the expected results for the given problem statement. It removes the need for explicit splitting with `', '` or `' '` and ensures that any punctuation or spaces remaining with the words are ignored. This allows it to handle various input scenarios gracefully.