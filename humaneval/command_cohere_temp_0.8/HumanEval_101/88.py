```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes regular expressions with the `re.findall()` function to efficiently split the string into words based on one or more alphanumeric characters (`\w+`). This ensures that each word is captured as a separate element in the resulting list, regardless of whether commas or spaces separate the words in the input string.

The provided example tests, meant to be executed using the `pytest` framework, demonstrate the correctness of this approach. The test cases examine various scenarios, including strings with different punctuation and whitespace, confirming the function's ability to extract words accurately.

By employing regular expressions in this way, the `words_string` function achieves a concise and reliable solution to the problem. The resulting code is concise, efficient, and adaptable to various scenarios involving string splitting.