```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach leverages regular expressions to match individual "word" patterns using the `\b\w+\b` syntax, which ensures that only word-containing strings are captured. This effectively handles various types of separators, including commas and spaces.

The function then uses the `re.findall()` method to collect all instances of the pattern in the input string, resulting in a list of words. This solution is both effective and concise.

For example, the result of `words_string("Hi, my name is John")` will be `["Hi", "my", "name", "is", "John"]`. 

This approach ensures that even complex sentences with varying separations between words will be accurately processed.