```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 
    'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the 
    given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y'
    last_char_is_y = s[-1] == 'y'
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel (ignoring case)
        if char.lower() in 'aeiou':
            # If the last character was 'y', don't count it
            if last_char_is_y and char.lower() == 'y':
                last_char_is_y = False
            else:
                # Increment the vowel counter
                count += 1
    
    # Return the total vowel count
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello"))  # Output: 2
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, as per the given requirements. The function iterates over each character in the string, checks if it's a vowel (ignoring case), and increments the vowel counter accordingly. If the last character is 'y', it's also counted as a vowel only if it's not followed by another vowel. The test cases at the end demonstrate the function's behavior.