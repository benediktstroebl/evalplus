```python
def is_last_char_y(s):
    """Helper function to check if the last character of a string is 'y'."""
    return len(s) > 0 and s[-1].lower() == 'y'

def vowels_count(s):
    """Count the number of vowels in a word.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
        elif is_last_char_y(s) and char.lower() == 'y':
            count += 1
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("Yay"))    # Output: 1
print(vowels_count("A"))      # Output: 1
print(vowels_count(""))       # Output: 0
```

This script defines two functions: `is_last_char_y` checks if the last character of a string is 'y', and `vowels_count` uses this helper function to count the number of vowels in a given string. It takes into account the special case where 'y' is a vowel if it appears at the end of the string. The script also includes example usage to demonstrate the functionality.