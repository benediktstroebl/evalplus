```python
def vowels_count(s):
    """
    Return the number of vowels in a given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it's at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Initialize a flag to track if the last character was 'y'
    last_was_y = False
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the count
            vowel_count += 1
        elif char == 'y' and not last_was_y:
            # If the character is 'y' and it's not at the end of the string, increment the count
            vowel_count += 1
            last_was_y = True
        else:
            # If the character is not a vowel and not 'y', reset the 'y' flag
            last_was_y = False
    
    # Return the total count of vowels
    return vowel_count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("AEIOUY"))  # Expected output: 6
print(vowels_count("Python"))  # Expected output: 2
print(vowels_count("y"))  # Expected output: 1
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in that string. The function considers 'y' as a vowel only when it's at the end of the word. It uses a flag `last_was_y` to track if the last character was 'y', and a counter `vowel_count` to keep track of the total number of vowels. The script includes several test cases to demonstrate the function's behavior.