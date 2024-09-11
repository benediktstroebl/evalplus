```markdown
### Longest String in a List
#### Problem Description
Out of a list of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input list is empty.

#### Solution
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string in a list. In case of a tie, return the first string.
    Return None if the list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    longest_string = strings[0]  # Initialize the longest string as the first one
    for string in strings[1:]:  # Iterate over the rest of the list
        if len(string) > len(longest_string):  # Check if the current string is longer
            longest_string = string  # Update the longest string

    return longest_string  # Return the longest string

# Example usage:
print(longest([]))  # Should print: None

print(longest(['a', 'b', 'c']))  # Should print: 'a'

print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

#### Explanation
This solution iterates over the input list, keeping track of the longest string encountered so far. If the list is empty, it returns `None`. If multiple strings have the same maximum length, it returns the first one encountered.