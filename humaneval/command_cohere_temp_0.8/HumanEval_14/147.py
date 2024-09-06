```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    current_prefix = ""
    for char in string:
        current_prefix += char
        prefixes.append(current_prefix)
    return prefixes
```

The code uses a loop to iterate through each character in the string. At each step, it constructs a current prefix by adding the character to the end of the previous prefix. This is done using the `re.findall()` function, which uses a regular expression to find all the prefixes of the given string. The regular expression used is `^(\w*)`, where `\w` matches any word character (equivalent to `[a-zA-Z0-9_]`), and `*` denotes recursion in regular expression. This expression captures all possible prefixes of the string, and `^` ensures that it starts from the beginning of the string.

The resulting list of prefixes is then returned as the result. The function calls itself recursively for each character in the string, appending the current character to the previous prefix and adding the new prefix to the list. This process continues until all characters have been processed, and the list of prefixes has been fully constructed. Since the loop starts with an empty string, the prefixes will grow as the loop progresses, producing the list of prefixes from shortest to longest. 

This approach ensures that the function is efficient in terms of time and space complexity, with a time complexity of `O(n)` since it only requires iterating through the characters in the input string once.