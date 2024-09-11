```python
# Vowels Count Problem
# ======================

# Define a function to count vowels in a given string
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): Input string for which the vowel count is to be calculated.

    Returns:
    int: Number of vowels in the input string.
    """
    # Convert the string to lowercase to handle case-insensitive matching
    s = s.lower()
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Check if the last character is 'y'
    if len(s) > 0 and s[-1] == 'y':
        # If 'y' is at the end, decrement the length and consider it as a vowel
        for char in s[:-1]:
            if char in 'aeiou':
                vowel_count += 1
        # Add 1 to the count for the last 'y'
        vowel_count += 1
    else:
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # Increment the vowel count if the character is a vowel
                vowel_count += 1
    
    # Return the total vowel count
    return vowel_count

# Example usage
if __name__ == "__main__":
    print(vowels_count("abcde"))  # Output: 2
    print(vowels_count("ACEDY"))  # Output: 3
```

This script defines the `vowels_count` function, which takes a string as input, counts the number of vowels (including 'y' if it's at the end), and returns the count. It includes example usage to demonstrate the function's behavior.