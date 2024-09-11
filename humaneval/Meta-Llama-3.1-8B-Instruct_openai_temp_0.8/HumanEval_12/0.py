```markdown
### Longest String in a List
#### A Python script to find the longest string in a list of strings.

```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    # Check if the list is empty
    if not strings:
        return None

    # Initialize the longest string as the first string in the list
    longest_str = strings[0]

    # Iterate over the list of strings
    for s in strings:
        # If the length of the current string is greater than the longest string found so far
        if len(s) > len(longest_str):
            # Update the longest string
            longest_str = s

    # Return the longest string
    return longest_str


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the input list is empty, it returns `None`. The `if __name__ == "__main__":` block contains test cases to verify the correctness of the function.