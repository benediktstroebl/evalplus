Here is a Python script that meets the requirements:
```markdown
## same_chars Function

### Description

Check if two words have the same characters.

### Code

```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    
    Args:
    s0 (str): The first word.
    s1 (str): The second word.
    
    Returns:
    bool: True if the words have the same characters, False otherwise.
    """
    # Remove white spaces and convert to lower case
    s0 = s0.replace(' ', '').lower()
    s1 = s1.replace(' ', '').lower()
    
    # Remove duplicate characters
    s0 = ''.join(dict.fromkeys(s0))
    s1 = ''.join(dict.fromkeys(s1))
    
    # Check if characters are the same
    return sorted(s0) == sorted(s1)

# Example use cases
if __name__ == "__main__":
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
    print(same_chars('abcd', 'dddddddabc'))  # True
    print(same_chars('dddddddabc', 'abcd'))  # True
    print(same_chars('eabcd', 'dddddddabc'))  # False
    print(same_chars('abcd', 'dddddddabce'))  # False
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

### Explanation

This script defines a function `same_chars` that takes two strings `s0` and `s1` as input. It first removes any white spaces from the strings and converts them to lower case to ensure the comparison is case-insensitive.

Then it removes any duplicate characters from the strings by converting them to dictionaries, which automatically removes any duplicate keys. Finally, it sorts the remaining characters in each string and checks if they are the same.

The example use cases demonstrate the function's behavior with different inputs.