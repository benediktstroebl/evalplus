```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Ensure the string contains at least one character
    if not s:
        return 0
    
    # List of uppercase vowels
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # Initialize count and iterate through the string
    count = 0
    for i, char in enumerate(s):
        if char.isupper() and char in vowels and (i % 2 == 0):
            count += 1
    
    return count
```

The solution leverages the `enumerate()` function to track character indices while iterating through the string, enabling the check for even indices. The function checks if each character is an uppercase vowel using the `isupper()` method and membership in the `vowels` list. The result is the count of uppercase vowels in even indices.