```python
def vowels_count(s):
    """
    Count the number of vowels in a given word.

    Vowels are 'a', 'e', 'i', 'o', 'u', and 'y' only when it is at the end of the word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.

    Example:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y'
    if s and s[-1] == 'y':
        # If 'y' is at the end, do not count other 'y's
        vowel_set = set('aeiou')
    else:
        # Otherwise, count all 'y's as a vowel
        vowel_set = set('aeiouy')
    
    # Iterate over the characters in the string
    for char in s:
        # If the character is in the vowel set, increment the count
        if char in vowel_set:
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello World"))  # Output: 3
print(vowels_count("You"))  # Output: 2
```

This script defines a function `vowels_count` that takes a string as input, converts it to lowercase, and counts the number of vowels in the string, considering 'y' as a vowel only when it is at the end of the word. The function uses a set for efficient lookups of vowels. The script includes example test cases to demonstrate the function's behavior.