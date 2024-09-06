```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach leverages regular expressions to match individual "word" sequences using the `\b` boundary matcher and the `\w+` sequence matcher to identify word sequences separated by commas and/or spaces. 

The resulting list of matched sequences is returned as an array. 

This approach handles edge cases and deviations in the problem specification, such as different types of separators or even leading/trailing separators. 
Let's move to the next problem if you want.