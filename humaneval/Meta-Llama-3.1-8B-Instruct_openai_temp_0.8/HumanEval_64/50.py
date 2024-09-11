```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    A vowel is 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to track if the last character was 'y'
    last_was_y = False
    
    # Iterate over the characters in the string
    for i in range(len(s)):
        # Check if the character is a vowel
        if s[i] in 'aeiou':
            count += 1
        # If the character is 'y' and it's not at the end of the string, reset the flag
        elif s[i] == 'y' and i!= len(s) - 1:
            last_was_y = False
        # If the character is 'y' and it's at the end of the string, increment the count
        elif s[i] == 'y' and i == len(s) - 1:
            count += 1
        # If the character is not a vowel or 'y', reset the flag
        else:
            last_was_y = False
    
    return count


# Test cases:
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, according to the problem description. The function iterates over the characters in the string, incrementing the vowel count whenever it encounters a vowel or a 'y' at the end of the string.