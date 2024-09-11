```markdown
### Same Characters Checker
#### A Python script to check if two words have the same characters
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
    
    # Convert the strings to sets, which automatically removes duplicates
    # Then compare the sets
    return set(s0) == set(s1)


# Example use cases
if __name__ == "__main__":
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
    print(same_chars('abcd', 'dddddddabc'))  # True
    print(same_chars('dddddddabc', 'abcd'))  # True
    print(same_chars('eabcd', 'dddddddabc'))  # False
    print(same_chars('abcd', 'dddddddabce'))  # False
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```
This script uses Python's built-in `set` type to check if two strings have the same characters. The `set` type automatically removes duplicates, so if two strings have the same characters, their corresponding sets will be equal. If the strings have different characters, their corresponding sets will be unequal. The script includes example use cases to demonstrate its functionality.