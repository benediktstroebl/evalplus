```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u' and 'y' is also a vowel if it's at the end of the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    """
    # Convert the string to lowercase to handle both lower and upper case vowels
    s = s.lower()
    
    # Initialize a counter for the number of vowels
    count = 0
    
    # Check if the last character of the string is 'y'
    if s and s[-1] == 'y':
        # If it's the last character, increment the counter
        count += 1
        # Remove the last character from the string
        s = s[:-1]
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it's a vowel, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("noy"))    # Expected output: 2
print(vowels_count("y"))      # Expected output: 1
print(vowels_count(""))       # Expected output: 0
print(vowels_count("aAeEiIoOuU"))  # Expected output: 10
```