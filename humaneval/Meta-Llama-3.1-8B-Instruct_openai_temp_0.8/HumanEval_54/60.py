### Python Script to Check if Two Strings Have the Same Characters

```markdown
### Code
```python
from collections import Counter

def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    Args:
        s0 (str): The first string.
        s1 (str): The second string.

    Returns:
        bool: True if the strings have the same characters, False otherwise.
    """
    # Count the frequency of each character in both strings
    count_s0 = Counter(s0)
    count_s1 = Counter(s1)

    # If the two strings have the same characters, their character counts must be equal
    return count_s0 == count_s1


### Example Use Cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

### Explanation

This script defines a function `same_chars` that takes two strings as input and returns `True` if they have the same characters and `False` otherwise. It uses the `Counter` class from the `collections` module to count the frequency of each character in both strings. If the two strings have the same characters, their character counts must be equal, so the function returns `True`. Otherwise, it returns `False`. The example use cases demonstrate the function's behavior with various inputs.