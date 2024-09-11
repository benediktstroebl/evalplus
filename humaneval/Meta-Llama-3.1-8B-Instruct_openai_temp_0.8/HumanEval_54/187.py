### Same Characters Function
This Python script defines a function `same_chars` that checks if two input strings have the same characters, regardless of order and count.

```markdown
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    
    Args:
    s0 (str): The first input string.
    s1 (str): The second input string.
    
    Returns:
    bool: True if the strings have the same characters, False otherwise.
    """
    # Convert both strings to sets to remove duplicates and ignore order
    set0 = set(s0)
    set1 = set(s1)
    
    # If the two sets are equal, it means the strings have the same characters
    return set0 == set1

# Test cases
if __name__ == "__main__":
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
    print(same_chars('abcd', 'dddddddabc'))  # True
    print(same_chars('dddddddabc', 'abcd'))  # True
    print(same_chars('eabcd', 'dddddddabc'))  # False
    print(same_chars('abcd', 'dddddddabce'))  # False
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This script works by converting both input strings to sets, which automatically removes any duplicate characters and ignores the order of characters. It then checks if the two sets are equal. If they are, the function returns True, indicating that the input strings have the same characters. Otherwise, it returns False.