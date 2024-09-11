```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    
    # Convert the string to lowercase to handle uppercase letters
    s = s.lower()
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the vowel count
            vowel_count += 1
        # Check if the character is 'y' and it's at the end of the string
        elif char == 'y' and s.endswith(char):
            # If the character is 'y' and it's at the end of the string, increment the vowel count
            vowel_count += 1
    
    # Return the total vowel count
    return vowel_count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines the `vowels_count` function to count the number of vowels (including 'y' at the end of the string) in a given string. It converts the string to lowercase, then iterates over each character. If a character is a vowel, it increments the vowel count. If a character is 'y' and it's at the end of the string, it also increments the vowel count. Finally, it returns the total vowel count.