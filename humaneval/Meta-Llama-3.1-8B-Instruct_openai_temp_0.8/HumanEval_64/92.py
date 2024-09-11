```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it's at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the input string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, count it as a vowel
            count += 1
        
        # Count the occurrences of 'a', 'e', 'i', 'o', 'u'
        for vowel in 'aeiou':
            count += s.count(vowel)
    
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("Hello"))  # Expected output: 2
print(vowels_count("Yay"))    # Expected output: 1
print(vowels_count(""))       # Expected output: 0
print(vowels_count("a"))      # Expected output: 1
```