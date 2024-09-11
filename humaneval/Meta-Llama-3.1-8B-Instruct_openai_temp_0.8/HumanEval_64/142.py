### Vowels Counter Script
```markdown
# vowels_count.py

FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    A vowel in this case is 'a', 'e', 'i', 'o', 'u'. 
    'y' is also considered a vowel when it is at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle uppercase letters
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou' or (char == 'y' and s[-1] == 'y'):
            # If the character is a vowel, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function handles both lowercase and uppercase letters, and considers 'y' as a vowel when it is at the end of the word. The script also includes example usage to demonstrate the function's behavior.