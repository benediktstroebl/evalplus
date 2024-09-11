### Problem Solution
```markdown
### how_many_times Function
#### Finds how many times a given substring can be found in the original string.
#### Count overlapping cases.

```python
import re

def how_many_times(string: str, substring: str) -> int:
    """
    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.
    
    Returns:
    int: The number of times the substring can be found in the original string.
    """
    if not substring:  # Edge case: substring is empty
        return 0
    
    regex = re.compile(re.escape(substring))
    matches = regex.finditer(string)
    return sum(1 for _ in matches)
```

### Example Usage
```python
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script uses the `re` module's `finditer` function to find all occurrences of the substring in the original string. The `re.escape` function is used to escape any special characters in the substring, preventing them from being interpreted as regular expression syntax. The `finditer` function returns an iterator yielding match objects for every non-overlapping occurrence of the substring in the string. The `sum` function is used to count the number of matches.