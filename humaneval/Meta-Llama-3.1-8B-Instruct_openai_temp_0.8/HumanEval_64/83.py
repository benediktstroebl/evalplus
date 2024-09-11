### Vowels Count Function
```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only when it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The count of vowels in the string.
    """
    s = s.lower()  # Convert the string to lowercase to simplify vowel detection
    vowel_count = 0  # Initialize the vowel count
    is_end_of_string = False  # Flag to check if 'y' is at the end of the string

    # Check if 'y' is at the end of the string
    if len(s) > 0 and s[-1] == 'y':
        is_end_of_string = True

    # Count the vowels
    for char in s:
        if char in 'aeiou' or (is_end_of_string and char == 'y'):
            vowel_count += 1

    return vowel_count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("AEIOUY"))  # Output: 6
```
This script defines a function `vowels_count` that takes a string `s` as input and returns the count of vowels in the string. It first checks if the last character of the string is 'y' and sets a flag `is_end_of_string` accordingly. It then iterates over the string, counting the vowels and considering 'y' as a vowel only when it's at the end of the string.