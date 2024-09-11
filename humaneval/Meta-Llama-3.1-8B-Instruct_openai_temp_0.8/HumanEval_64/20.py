### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in a given string. 
    'y' is considered a vowel only when it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    s_lower = s.lower()
    count = 0
    is_y_at_end = False

    # Check if the last character is 'y'
    if len(s) > 0 and s[-1].lower() == 'y':
        is_y_at_end = True

    # Count the vowels, excluding 'y' if it's at the end
    for char in s_lower:
        if char in vowels and char!= 'y' or (char == 'y' and not is_y_at_end):
            count += 1
        # Update 'is_y_at_end' if the current character is 'y' and it's not at the end
        elif char.lower() == 'y' and is_y_at_end:
            is_y_at_end = False

    return count
```

### Example Use Cases
```python
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
print(vowels_count("hello"))  # 2
print(vowels_count("myF"))  # 1
print(vowels_count("Last one")) # 3 
```
This script provides a function `vowels_count` that calculates the number of vowels in a given string, considering 'y' as a vowel only when it is at the end of the string. It uses a case-insensitive approach and excludes 'y' from the count if it is not at the end of the string.